-- WITH tb_subse_mediana AS (

--     SELECT qtdPontos 
--     FROM points
--     ORDER BY qtdPontos
--     LIMIT 2
--     OFFSET 2500 -- ELE PULA n ELEMENTOS
-- )


-- MEDIANA

WITH tb_subset_mediana AS (

    SELECT qtdPontos 
    FROM points
    ORDER BY qtdPontos
    LIMIT 1 + (SELECT COUNT(*)%2 == 0 FROM points)
    OFFSET (SELECT COUNT(*)/2 FROM points)

),

tb_mediana AS ( 
    SELECT AVG(qtdPontos) AS Mediana
    FROM tb_subset_mediana
),

-- 1o QUARTIL

tb_subset_01_quartil AS (
    SELECT qtdPontos
    FROM points 
    ORDER BY qtdPontos
    LIMIT 1 + (SELECT COUNT(*)%4 == 0 FROM points)
    OFFSET (SELECT 1 * (COUNT(*)/4) FROM points)
),

tb_quartil_01 AS (
    SELECT AVG(qtdPontos) AS quartil_01
    FROM tb_subset_01_quartil
),

-- 3o QUARTIL

tb_subset_03_quartil AS (
    SELECT qtdPontos
    FROM points
    ORDER BY qtdPontos
    LIMIT 1 + (SELECT COUNT(*)%4 == 0 FROM points)
    OFFSET (SELECT 3 * (COUNT(*)/4) FROM points)
),

tb_quartil_03 AS (
    SELECT AVG(qtdPontos) AS quartil_03
    FROM tb_subset_03_quartil
),

-- MIN MAX AVG

tb_stats AS(
    SELECT MIN(qtdPontos) AS minimo,
           AVG(qtdPontos) AS media,
           MAX(qtdPontos) AS maximo
    FROM points
)

-- MOSTRANDO

SELECT *
FROM tb_stats, tb_quartil_01, tb_mediana, tb_quartil_03
