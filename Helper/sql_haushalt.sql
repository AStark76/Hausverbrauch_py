--SELECT d.id, DATE, value FROM categories AS c left JOIN data AS d ON d.cat_Id = c.Id WHERE (c.cat_name = "Strom");
SELECT * FROM categories;
