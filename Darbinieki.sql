insert or ignore into darbinieki values("D_03","Jānis","Zvejnieks","432679","31","28.03.2004",500);
insert or ignore into darbinieki values("D_04","Ilze","Lapa","583481","47","13.09.2013",250);
select distinct darbinieka_id, vards, uzvards, telefons, vecums, liguma_datums, bonuss from darbinieki;
select vards, uzvards, bonuss from darbinieki;
select max(bonuss)from darbinieki;
select avg(vecums) from darbinieki;
select min(vecums) from darbinieki;
select sum(bonuss) from darbinieki;
