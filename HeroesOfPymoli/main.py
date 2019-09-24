# importing necessary modules to manipulate numbers
import pandas as pd 
import numpy as np 

#Reading to file and creating the main dataframe with all the information
file_path="Resources/purchase_data.csv"
pymoli_df=pd.read_csv(file_path)
#print(pymoli_df.head())

print("__________________________________________________________________________")
#__________________________________________________________________________
#1) - PLAYER COUNT
#total number of players
unique_player=pymoli_df["SN"].unique()
player_count=len(unique_player)
total_players=pd.DataFrame({"Total Players": [player_count]})
print(total_players)

print("__________________________________________________________________________")
#__________________________________________________________________________
#2) - PURCHASING ANALYSIS(TOTAL)
##Preparing all the calculations for the total values dataframe
purchase_count=pymoli_df["SN"].count()
purchase_sum=pymoli_df["Price"].sum()
value_per_purchase=purchase_sum/purchase_count
unique_items=len(pymoli_df["Item ID"].unique())

#Incorporating the values calculated and the formating into a new dataframe
total_analysis=pd.DataFrame({
    "Number of unique Items": [unique_items],
    "Average Price": [value_per_purchase],
    "Total Purchase Number": [purchase_count],
    "Total Revenue": [purchase_sum]
})

#formating data to be displayed better for the Average Price and Total Rvennue
total_analysis["Average Price"] = total_analysis["Average Price"].map("${:,.2f}".format)
total_analysis["Total Revenue"] = total_analysis["Total Revenue"].map("${:,.2f}".format)

#Printing 2) Results
print(total_analysis)
 
print("__________________________________________________________________________")
#__________________________________________________________________________
#3) GENDER DEMOGRAPHICS
#group the original df by Gender using unique values of user name, to avoid repetition
gender_count=pymoli_df.groupby("Gender")["SN"].nunique()

#Creating new df with the selection made above
gender_df=pd.DataFrame(gender_count)

#Renaming the SN column, to indicate the count of unique users by gender
gender_df.rename(columns={'SN':'Total Count'}, inplace=True)

#establishing the total of unique players to make further calculations
unique_players_sum=gender_df["Total Count"].sum()

#Creating a new column for the percentage an loping trough Total Count and the variable above to make the calculation
gender_df["Gender Percent"]=(gender_df["Total Count"]/unique_players_sum)*100

#formating percentage values
gender_df["Gender Percent"] = gender_df["Gender Percent"].map("{:,.2f}%".format)

#print 3) results df
print(gender_df)

print("__________________________________________________________________________")
#__________________________________________________________________________
#4) Purchase Analysis (Gender)
#Grouping original df by gender, including every single transaction
purchase_count_gender=pymoli_df.groupby('Gender')['Item ID'].count()

#Calculating average price paid per gender
#Calculating the total value purchased by gender
avrg_price_gender=pymoli_df.groupby('Gender')['Price'].mean()
revenue_per_gender=pymoli_df.groupby('Gender')['Price'].sum()

#Creating new data frame for this analysis, initially with the transactions count per gender.
gender_grouped_df=pd.DataFrame(purchase_count_gender)

#Renaming first column, to describe the purchase count
gender_grouped_df.rename(columns={"Item ID":"Purchase Count"}, inplace=True)

#creating new column to insert the average price per gender transactions
#creating new column to insert the total value spent by gender transactions
#Creating new  column to insert average purchase value per gender by each individual
gender_grouped_df["Average Purchase Price"]=avrg_price_gender
gender_grouped_df["Total purchase value"]=revenue_per_gender
gender_grouped_df["Avg Total Purchase per person"]=revenue_per_gender/gender_count

#Formating the numbers dusplayed
gender_grouped_df["Average Purchase Price"] = gender_grouped_df["Average Purchase Price"].map("${:,.2f}".format)
gender_grouped_df["Total purchase value"] = gender_grouped_df["Total purchase value"].map("${:,.2f}".format)
gender_grouped_df["Avg Total Purchase per person"]= gender_grouped_df["Avg Total Purchase per person"].map("${:,.2f}".format)

#printing the results for 4)
print(gender_grouped_df)

print("__________________________________________________________________________")
#__________________________________________________________________________
#5) AGE DEMOGRAPHICS 
#Setting up variables to categorize the data withing specific age ranges
#Inserting a new column that shows bin labels according to Age reange
bins=[0,9, 14, 19, 24, 29, 34, 39, 45]
bin_labels=["<10","10-14","15-19","20-24", "25-29", "30-34", "35-39", "40+"]
pymoli_df['Age range']=pd.cut(pymoli_df['Age'], bins, labels=bin_labels)

#Cheating new df to manipulate without changing the original
age_df=pd.DataFrame(pymoli_df)

#Counting individuals by age range
#Inserting/changing a label for this column "Total Count"
age_grouped=age_df.groupby("Age range")[["SN"]].nunique()
age_grouped.rename(columns={"SN":"Total Count"}, inplace=True)

#Creating new column that displays the percentage of players per age range
age_grouped["Percentage of Players"]=(age_grouped["Total Count"]/age_grouped["Total Count"].sum())*100

#Formatting diplayed percentage numbers
age_grouped["Percentage of Players"]= age_grouped["Percentage of Players"].map("{:,.2f}%".format)

#Printing results for 5)
print(age_grouped)

print("__________________________________________________________________________")
#__________________________________________________________________________
#6) AGE PURCHASE ANALYSIS
#using age_df created in the step below, group into a new data frame, counting all transactions age by Age range
#Replacing the name of the column to suit the analysis, the df will display the range of ages and the total count of purchases within the ranges
age_grouped2=age_df.groupby("Age range")[["Age"]].count()
age_grouped2.rename(columns={"Age":"Purchase Count"}, inplace=True)

#Doing all calculations to be inserted into the column later on 
age_count=pymoli_df.groupby("Age range")["SN"].nunique()
avrg_price_age=age_df.groupby('Age range')['Price'].mean()
revenue_per_age=pymoli_df.groupby('Age range')['Price'].sum()

#Inserting all the calculations into respectively named columns
age_grouped2["Average Purchase Price"]=avrg_price_age
age_grouped2["Total Purchase Value"]=revenue_per_age
age_grouped2["Avg Total Purchase per Person"]=revenue_per_age/age_count

#Formatting hte displayed information 
age_grouped2["Average Purchase Price"]=age_grouped2["Average Purchase Price"].map("${:,.2f}".format)
age_grouped2["Total Purchase Value"]=age_grouped2["Total Purchase Value"].map("{:,.2f}".format)
age_grouped2["Avg Total Purchase per Person"]=age_grouped2["Avg Total Purchase per Person"].map("${:,.2f}".format)

#printing results for 6)
print(age_grouped2)

print("__________________________________________________________________________")
#__________________________________________________________________________
#7) TOP SPENDERS
#Setting initial df that displays the number of transactions grouped by Username
#Rename the counting column so you don't have index with same name
spenders_df=pymoli_df.groupby("SN")[["SN"]].count()
spenders_df.rename(columns={"SN":"Purchase Count"}, inplace=True)

#Doing all calculations to be inserted into the column later on 
avrg_price_sn=pymoli_df.groupby('SN')['Price'].mean()
revenue_per_sn=pymoli_df.groupby('SN')['Price'].sum()

#Inserting all the calculations into respectively named columns
spenders_df["Average Purchase Price"]=avrg_price_sn
spenders_df["Total Purchase Value"]=revenue_per_sn

#Sorting data by the gamers who spent more in the game
top_spenders=spenders_df.sort_values( "Total Purchase Value", ascending=False)

#Formatting the monetary displayed information
top_spenders["Average Purchase Price"]=top_spenders["Average Purchase Price"].map("${:,.2f}".format)
top_spenders["Total Purchase Value"]=top_spenders["Total Purchase Value"].map("${:,.2f}".format)

#Printing results for 7)
print(top_spenders.head())

print("__________________________________________________________________________")
#__________________________________________________________________________
#8) MOST POPULAR ITEMS
#Creating new df with double groupby, and replaccing the name of the column so it's different from Index
popular_df=pymoli_df.groupby(["Item ID","Item Name"])[['Item ID']].count()
popular_df.rename(columns={"Item ID":"Purchase Count"}, inplace=True)

#Inserting all the calculations into respectively named columns
popular_df['Total Purchase Value']=pymoli_df.groupby(['Item ID',"Item Name"])[['Price']].sum()
popular_df['Item Price']=popular_df['Total Purchase Value']/popular_df['Purchase Count']

#Sorting data by the gamers who spent more in the game
most_popular=popular_df.sort_values( "Purchase Count", ascending=False)

#Formatting the monetary displayed information
most_popular['Total Purchase Value']=most_popular['Total Purchase Value'].map("${:,.2f}".format)
most_popular['Item Price']=most_popular['Item Price'].map("${:,.2f}".format)

#Printing results for 8)
print(most_popular.head())

print("__________________________________________________________________________")
#__________________________________________________________________________
#9) MOST PROFITABLE ITEMS
profitable_df=popular_df
most_profitable=profitable_df.sort_values( "Total Purchase Value", ascending=False)
print(most_profitable.head())