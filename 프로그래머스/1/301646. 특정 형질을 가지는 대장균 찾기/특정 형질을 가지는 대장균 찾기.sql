select count(*) as count
from ECOLI_DATA
where substring(bin(genotype), -2, 1) = 0 and (substring(bin(genotype), -3, 1) = 1 or substring(bin(genotype), -1, 1) = 1)