import pandas as pd
import imdb

df = pd.read_excel(r'C:\letsupgrage assignment\cast2.xlsx')
df.drop_duplicates()
print(df.head())
print(df.isna().sum())
print(df.isnull().sum())
print(df.describe())
print(df.info())
print("\n1.How many movies are listed in the titles dataframe?")
print(df.title.value_counts())
print("\n2.What are the earliest two films listed in the titles dataframe?")
print(df.sort_values('year').head(2))
print("\n 3.How many movies have the title 'Hamlet'?")
print(len(df[df.title == 'Hamlet']))
print("\n 4.How many movies have the title 'North by Northwest'?")
print((df[df.title == 'North by Northwest']))
print("\n 5.When was the first movie titled 'Hamlet' made?")
print(df[df.title == 'Hamlet'].sort_values('year').head(1))
print("\n 6.List all of the 'Treasure Island' movies from earliest to most recent.")
print(df[df.title == 'Treasure Island'].sort_values('year'))
print("\n 7.How many movies were made in the year 1950?")
print(df[df.year==1960].count())
print("\n8.How many movies were made in the year 1960")
print(df[df.year == 1950].count())
print("\n 9.How many movies were made from 1950 through 1959?")
bool_series = df["year"].between(1950, 1959).count()
print(bool_series)
print("\n 10.In what years has a movie titled 'Batman' been released?")
df2 = pd.read_csv(r'C:\letsupgrage assignment\titles.csv')
df1 = df2[df2['title'] == 'Batman']
print(df1)
df3 = pd.read_excel(r"C:\letsupgrage assignment\cast.xlsx")
df3.drop_duplicates()
print("\n11.How many roles were available for actor  in the 1950s?")
print(df3[df3.type == 'actor'].count())
print("\n12.How many roles were available for actresses  in the 1950s?")
print(df3[df3.type == 'actress'].count())
print("\n13.How many leading roles (n=1) were available from the beginning of film history through 1980?")
new1 = (df3[df3.year == 1980])
print(new1[new1.n == 1].count())
print("\n14.How many roles in the movie 'Inception' are NOT ranked by an 'n' value?")
new3 = (df3[df3.title == "Inception"])
print(new3[new3.n == 0].count())
print("\n15.But how many roles in the movie 'Inception' did receive an 'n' value?")
print(new3[new3.n != 0].count())
print("\n16.List the supporting roles (having n=2) played by Cary Grant in the 1940s, in order by year.")
new2 = (df3[df3.name == 'Cary Grant'])
new5 = (new2[new2.n == 2])
print(new5[new5.year == 1940])
print("\n17.List the leading roles that Cary Grant played in the 1940s in order by year.")
new6 = (new2[new2.n == 1])
print(new6[new6.year == 1940])
print("\n18.Now display the entire cast, in 'n'-order, of the 2007 version of 'Sleuth'")
new7 = (df3.sort_values('n'))
new7 = (new7[new7.title == "Sleuth"])
print(new7[new7.year == 2007])
print("\n19.Display the entire cast, in 'n'-order, of the 1972 film 'Sleuth'")
print(new7[new7.year == 1972])
print("\n20.How many 'Hamlet' roles have been listed in all film credits through history?")
print(df3[df3.character == 'Hamlet'])
print("\n21.Display the cast of 'North by Northwest' in their correct 'n'-value order, ignoring roles that did not earn a numeric 'n' value.")
new8 = (df3[df3.n != 0])
new8 = (new8.sort_values('n'))
new9 = (new8[new8.title == 'North by Northwest'])
print(new9)
print("\n22.How many non-leading roles were available through from the beginning of film history through 1980?")
new = (df3[df3.year == 1980])
new[new.n != 1].count()
print(new)
print("\n23.How many people have played an 'Ophelia'?")

ia = imdb.IMDb()  
name = "Ophelia" 
search = ia.search_movie(name) 
for i in search: 
    print(i) 


print("\n the next \n")
ia = imdb.IMDb()  
name = "Ophelia"  
search = ia.search_movie(name) 
 
for i in range(len(search)): 
    id = search[i].movieID 
    print(search[i]['title'] + " : " + id ) 

ia = imdb.IMDb() 
code = "5690810"
series = ia.get_movie(code) 
no = series.data['cast']
print(len(no))


print("\n24.How many people have played an 'The Dude'?")
ia = imdb.IMDb()  
name = "The Dude" 
search = ia.search_movie(name) 
for i in search: 
    print(i) 


print("\n the number of roles\n")
ia = imdb.IMDb()  
name = "The Dude"  
search = ia.search_movie(name) 
 
for i in range(len(search)): 
    id = search[i].movieID 
    print(search[i]['title'] + " : " + id ) 


ia = imdb.IMDb() 
code = "1939758"
series = ia.get_movie(code) 
no = series.data['cast']
print(len(no))

print("\n25.How many people have played an 'The Stranger'?")
ia = imdb.IMDb()  
name = "The Stranger" 
search = ia.search_movie(name) 
for i in search: 
    print(i) 


print("\n the number of roles\n")
ia = imdb.IMDb()  
name = "The Stranger"  
search = ia.search_movie(name) 
  
for i in range(len(search)): 
    id = search[i].movieID 
    print(search[i]['title'] + " : " + id ) 


ia = imdb.IMDb() 
code = "9698480"
series = ia.get_movie(code) 
no = series.data['cast']
print(len(no))




