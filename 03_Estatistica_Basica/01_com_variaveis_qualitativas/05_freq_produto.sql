WITH tb_freq_abs AS (

    SELECT descProduto,
        COUNT(idTransacao) AS FreqAbs

    FROM points

    GROUP BY descProduto

),

tb_freq_abs_cum AS (

    SELECT *,
        SUM(FreqAbs) OVER (ORDER BY descProduto) AS FreqAbsAcum,
        1.0 * FreqAbs / (SELECT SUM(FreqAbs) FROM tb_freq_abs) AS FreqRel
        -- o 1.0 serve para garantir que a divisão seja feita em ponto flutuante
    
    FROM tb_freq_abs

)

SELECT * ,
    SUM(FreqRel) OVER (ORDER BY descProduto) AS FreqRelAcum

FROM tb_freq_abs_cum