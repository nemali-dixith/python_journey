--Exploratory data analysis 
SELECT * FROM layoffs_staging
--which companies laidoff max and max percent laid off 
SELECT MAX(total_laid_off),MAX(percentage_laid_off)
FROM layoffs_staging
--if we order by funcs_raised_millions we can see how big some of these companies were
SELECT *
FROM layoffs_staging
WHERE percentage_laid_off = 1
ORDER BY funds_raised_millions DESC;
--
SELECT company,SUM(total_laid_off) AS total_laid
FROM layoffs_staging
GROUP BY company
ORDER BY 2 DESC;

SELECT MIN([date]),MAX([date])
FROM layoffs_staging
-- Companies with the most Total Layoffs
SELECT industry, SUM(total_laid_off) AS total_laid
FROM layoffs_staging
GROUP BY industry
ORDER BY 2 DESC;
-- location with the most Total Layoffs
SELECT location,SUM(total_laid_off) AS total_laid
FROM layoffs_staging
GROUP BY location
ORDER BY 2 DESC;
-- country with the most Total Layoffs
SELECT country,SUM(total_laid_off) AS total_laid
FROM layoffs_staging
GROUP BY country
ORDER BY 2 DESC;
-- specfic yrs with the most Total Layoffs
SELECT YEAR([date]),SUM(total_laid_off)AS total_laid
FROM layoffs_staging
GROUP BY YEAR([date])
ORDER BY 1 DESC;
--stage of a company
SELECT stage,SUM(total_laid_off)AS total_laid
FROM layoffs_staging
GROUP BY stage
ORDER BY 1 DESC;
--layoffs by months 
SELECT SUBSTRING([date],1,7) AS [MONTH],SUM(total_laid_off)
FROM layoffs_staging
WHERE SUBSTRING([date],1,7) IS NOT NULL
GROUP BY SUBSTRING([date],1,7)
ORDER BY 1 ASC
;
--companies laying off per year
SELECT company,YEAR([date])AS YEAR, SUM(total_laid_off) AS total_laid
FROM layoffs_staging
GROUP BY company,YEAR([date])
ORDER BY 3 DESC;

WITH Company_year AS
(
SELECT company,YEAR([date])AS YEAR, SUM(total_laid_off) AS total_laid
FROM layoffs_staging
GROUP BY company,YEAR([date])
),Company_Year_Rank AS
(SELECT *, DENSE_RANK() OVER (PARTITION BY year ORDER BY total_laid DESC) AS RANKING
FROM Company_year
WHERE year IS NOT NULL
)
SELECT * FROM Company_Year_Rank
WHERE RANKING <=5;
