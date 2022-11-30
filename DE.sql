create Table all_data AS            # 전체음식점 데이터를 하나의 Table로 만드는 쿼리문
    select * from 1_all union
    select * from 2_all union
    select * from 3_all union
    select * from 4_all union
    select * from 5_all union
    select * from 6_all union
    select * from 7_all;

Alter table all_data drop column 업태구분명;      # 전체음식점 데이터중 업태구분명 제거
Delete from all_data where 상세영업상태명 = '폐업';  # 상세영업상태에서 폐업인 데이터 제거



ALTER TABLE kakaomap                #카카오맵 데이터 변수명 변경
RENAME COLUMN 가게이름 to store;
ALTER  TABLE kakaomap
RENAME COLUMN 주소 to adress;
Alter Table kakaomap
    RENAME COLUMN store to place;

Alter Table yeskids                   # yeskidszone 변수명 변경
    RENAME COLUMN 음식점명 to place;



ALTER TABLE all_data                  # 전체 음식점 데이터 변수명 변경
    RENAME COLUMN 사업장명 to store;
Alter Table all_data
RENAME COLUMN 소재지전체주소 to adress1;
Alter Table all_data
RENAME COLUMN 도로명전체주소 to adress2;
Alter TABLE  all_data
    RENAME COLUMN store to place;





# 전체음식점 도로명주소의 Missing Data 해결
# 도로명 주소가 없는 곳은 지번주소로 대체하여 해결
alter table all_data add column adr varchar(100);
alter table all_data modify adr varchar(150);

select adress2, adress1,
       CASE
            WHEN adress2 is not NULL THEN adress2
            ELSE adress1
            End as adr
from all_data;

update all_data
set adr = case
              WHEN adress2 is not NULL THEN adress2
              ELSE adress1
end;




select * from MLnokids where place in (select adr from `all_data`);
select * from yeskids where place in (select adr from `all_data`);
select * from kakaomap where place in (select adr from `all_data`);




#mlplace 신뢰도가 0.9 이상인 장소의 DB를 생성
create table final_place
select place from final
    union
select place from kakaomap
    union
select place from MLnokids  #
    union
select place from yeskids;   # yeskidszone


# 기존의 데이터와 AI로 추출한 데이터를 결합
Create table final
select place from mlplace where confidence > 0.9;



# 결합된 데이터를 전체 음식점데이터와 비교하여 최종 Data 테이블 생성
create table last
select place, adr from `all_data` where place in (select place from final_place);



# select place, confidence,
# CASE WHEN confidence > 0.9 else null end place
# from mlplace;
#
# select place from mlplace where confidence > 0.9;

# select content, place,
#        CASE
#            WHEN place is not NULL THEN content
#            ELSE null
#            End as cont
# from 1_pre;
#
# alter table 1_pre add cont varchar(500) not null default '0';
