## 4. SQLite ##

select Rank,Major from recent_grads;

## 5. Specifying column order ##

select Major, Rank from recent_grads;

## 6. Practice: Select ##

select Rank,Major_code,Major,Major_category, Total from recent_grads;

## 7. Where ##

SELECT Major,ShareWomen
FROM recent_grads
WHERE ShareWomen > 0.5;

## 8. Practice: Where ##

select Major,Employed from recent_grads where Employed > 10000;

## 9. Limit ##

select Major from recent_grads where Employed > 10000 limit 10;