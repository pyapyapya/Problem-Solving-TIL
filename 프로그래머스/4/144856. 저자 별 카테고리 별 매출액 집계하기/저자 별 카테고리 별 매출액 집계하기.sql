with book_author as (
    select a.author_id, a.author_name, b.book_id, b.category, b.price, b.published_date
    from book b
    left join author a
    on b.author_id = a.author_id
), sales as (
    select book_id, sum(sales) sales_by_book
    from book_sales
    where sales_date between '2022-01-01' and '2022-01-31'
    group by book_id
), book_author_sales as (
    select b.author_id, b.author_name, b.category, b.price, s.sales_by_book
    from book_author b
    left join sales s
    on b.book_id = s.book_id
)

select author_id, author_name, category, sum(sales_by_book * price) total_sales
from book_author_sales
group by author_id, category
order by author_id asc, category desc