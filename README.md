# Basics of Python Programming in MSU - Autumn 2021 / Основы Python в МГУ - Осень 2021

**[Link to certificate](https://drive.google.com/file/d/1YIrroq_qH3uuRIcISHdHZuih2B9yCPOp/view?usp=sharing)** 
## Итоговая работа по анализу данных Coronaindex'a в России находится в final_work


**[Tinkoff CoronaIndex](https://index.tinkoff.ru/)** 
> Индекс деловой и потребительской активности в России. Показывает, как меняется жизнь в России ... под влиянием последствий пандемии: как трансформируются потребительские привычки, масштабы и обороты бизнеса, какие сферы и в каких регионах страны сокращаются или, наоборот, активно растут.


**Описание полей:**
* __auth_dt__ – бизнес-дата. Часть составного первичного ключа
* __state_name__ – российский регион. Часть составного первичного ключа
* __purchase_category_nm__ – категория трат. Часть составного первичного ключа
* __online_part__ - доля онлайн покупок, в %
* __online_regarding_avg__ - отклонение онлайн-потребительской активности в % от средней онлайн-потребительской активности в 2019, в %
* __offline_regarding_avg__ - отклонение оффлайн-потребительской активности в % от средней оффлайн-потребительской активности в 2019, в %
* __total_regarding_avg__ - отклонение  общей потребительской активности (онлайн+оффлайн) в % от средней общей потребительской активности в 2019, в %
* __coronaindex__ - величина коронаиндекса

## Были выполнены следующие задания:
* Найти 3 соответствия месяц-регион-год, у которых средний coronaindex за месяц наивысший, а также 3 соответствия месяц-регион-год, у которых средний coronaindex самый низкий. Далее для всех 6 комбинацийсравнить:
    * Как отличаются эти группы относительно онлайн и офлайн покупок? 
    * Как отличаются эти группы категории трат?
* Найти 1 регион с наивысшим и наименьшим разбросом значения coronaindex'a за все время. Далее, построить общий график, на котором присутствуют:
    * Среднее значение coronaindex'а за месяц;
    * Категории с наибольшим и наименьшим средним значением coronaindex'а за месяц;
    * Среднее значение coronaindex'а по всем регионам (state_name=All).
## (1) Показать состояние среднего значения индекса по регионам России за 2020 год на карте
* Для построения карты необходимы все регионы в одном формате, поправьте это расхождение для следующего пункта(можно из geojson'а)
* Добавить расширенную информацию на карту с регионами, например: топ-3 категории трат региона, долю онлайн / офлайн покупок.

## (2) В каких регионах деловая и потребительская активность сильно отличается от других?
* Что в этих регионах происходило на протяжении 2 лет: как активность отличалась от других регионов, например Москвы?
* Построить линейные графики по нескольким категориям трат и сравнить с другими регионами, например с Москвой?
* В каких регионах наоборот активность похожа? 

## (3) В какие месяцы и в каких категориях бизнеса происходили наибольшие взлеты и падения? 

<span style="color:green">__Открытый вопрос__:</span> от Вас требуется проанализировать данные и, относительно предыдущих вопросов, сформировать 3-5 гипотез и проверить их — отвергнуть или подтвердить.
