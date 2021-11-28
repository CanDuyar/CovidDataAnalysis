import pandas as pd
import numpy as np
import math

df2 = pd.read_csv("owid-covid-data.csv")


#CAN DUYAR 171044075
'''
If you want to see the output.txt, please use "python can_duyar_171044075.py > output.txt" on the terminal 
I also sent output.txt as document in addition to code.
'''

#Q11111111  How many countries the dataset has?

#Q22222222   When is the earliest date data are taken for a country? Which country is it?
print("Q2:\n")
df2.sort_values(by="date",inplace = True,ignore_index=True)
early_country = df2['location'][0]
early_date = df2['date'][0]
print("Country: ", early_country)
print("Date: ", early_date)

print("**************************************  Q18   *************************************")

df = pd.read_csv("owid-covid-data.csv")

print("Q1:\n")
numberOfCountries = len(df2['location'].unique())   #Q1
print(numberOfCountries)


print("***************************************************************************")




#Q3  How many cases are confirmed for each country so far? Print pairwise results of country and total cases.
print("Q3:\n")
unique_list = df['location'].unique()
index_sum = 0
cntrl = 0
for i in unique_list:
	check = 1
	count = np.count_nonzero(df['location']== i)
	index_sum += count

	print("Country: ",df['location'][index_sum-1])
	for x in range(cntrl,index_sum):
		if(check == count):
			print("Couldn't found a valid total cases data\n")
			break 

		if(not np.isnan(df['total_cases'][index_sum-check])):
			print("Total cases are confirmed: ",df['total_cases'][index_sum-check])
			print("\n")
			break
		else:
			check+=1
		cntrl = count	



print("***************************************************************************")


#Q4	How many deaths are confirmed for each country so far? Print pairwise results of country and total deaths	

print("Q4:\n")

unique_list2 = df['location'].unique()

index_sum2 = 0

cntrl = 0

for i in unique_list2:
	check = 1
	count2 = np.count_nonzero(df['location']== i)
	index_sum2 += count2
	print("Country: ",df['location'][index_sum2-1])
	
	for x in range(cntrl,index_sum2):
		if(check == count2):
			print("Couldn't found a valid total deaths data\n")
			break 
		
		if(not np.isnan(df['total_deaths'][index_sum2-check])):
			print("Total deaths are confirmed: ",df['total_deaths'][index_sum2-check])
			print("\n")
			break
	
		else:
			check+=1
		cntrl = count2

print("***************************************************************************")


# Q5 What are the average, minimum, maximum and variation values of the reproduction rates for each country?

print("Q5:\n")

unique_list2 = df['location'].unique()

index_sum2 = 0
control = 0
array = []

for i in unique_list2:
	count2 = np.count_nonzero(df['location']== i)
	index_sum2 += count2


	for x in range(control,index_sum2):
			array.append(df['reproduction_rate'][x])
	
	array = [x for x in array if math.isnan(x) == False]
	
	if(len(array)!=0):
		print("Country",end = "      ")
		print("minimum   maximum   average   variation")
		print(df['location'][control],end = "      ")
		print(round(np.min(array),3),end = "        ")
		print(round(np.max(array),3),end = "      ")
		print(round(np.average(array),3),end = "      ")
		print(round(np.var(array),3),end = "     ")
		print("\n")
		array.clear()

	control = index_sum2

print("***************************************************************************")


# Q6 What are the average, minimum, maximum and variation values of the icu patients (intensive care unit
#patients) for each country?

print("Q6:\n")

unique_list3 = df['location'].unique()

index_sum3 = 0
control2 = 0
array2 = []

for i in unique_list3:
	count3 = np.count_nonzero(df['location']== i)
	index_sum3 += count3


	for x in range(control2,index_sum3):
		array2.append(df['icu_patients'][x])

	array2 = [x for x in array2 if math.isnan(x) == False]
	if(len(array2)!=0):
		print("Country",end = "      ")
		print("minimum   maximum   average   variation")
		print(df['location'][control2],end = "      ")
		print(round(np.min(array2),3),end = "        ")
		print(round(np.max(array2),3),end = "      ")
		print(round(np.average(array2),3),end = "      ")
		print(round(np.var(array2),3),end = "     ")
		print("\n")
		array2.clear()

	control2 = index_sum3

print("***************************************************************************")

# Q7 What are the average, minimum, maximum and variation values of the hosp patients (intensive care unit
#patients) for each country?

print("Q7:\n")

unique_list3 = df['location'].unique()

index_sum3 = 0
control2 = 0
array2 = []

for i in unique_list3:
	count3 = np.count_nonzero(df['location']== i)
	index_sum3 += count3


	for x in range(control2,index_sum3):
			array2.append(df['hosp_patients'][x])

	array2 = [x for x in array2 if math.isnan(x) == False]
	if(len(array2)!=0):
		print("Country",end = "      ")
		print("minimum   maximum   average   variation")
		print(df['location'][control2],end = "      ")
		print(round(np.min(array2),3),end = "        ")
		print(round(np.max(array2),3),end = "      ")
		print(round(np.average(array2),3),end = "      ")
		print(round(np.var(array2),3),end = "     ")
		print("\n")
		array2.clear()

	control2 = index_sum3


print("***************************************************************************")

# Q8 What are the average, minimum, maximum and variation values of the weekly icu (intensive care unit)
#admissions for each country?

print("Q8:\n")

unique_list3 = df['location'].unique()

index_sum3 = 0
control2 = 0
array2 = []

for i in unique_list3:
	count3 = np.count_nonzero(df['location']== i)
	index_sum3 += count3


	for x in range(control2,index_sum3):
			array2.append(df['weekly_icu_admissions'][x])
	
	array2 = [x for x in array2 if math.isnan(x) == False]
	
	if(len(array2)!=0):
		print("Country",end = "      ")
		print("minimum   maximum   average   variation")
		print(df['location'][control2],end = "      ")
		print(round(np.min(array2),3),end = "        ")
		print(round(np.max(array2),3),end = "      ")
		print(round(np.average(array2),3),end = "      ")
		print(round(np.var(array2),3),end = "     ")
		print("\n")
		array2.clear()

	control2 = index_sum3

print("***************************************************************************")

# Q9 What are the average, minimum, maximum and variation values of the weekly hospital admissions for
#each country?

print("Q9:\n")

unique_list3 = df['location'].unique()

index_sum3 = 0
control2 = 0
array2 = []

for i in unique_list3:
	count3 = np.count_nonzero(df['location']== i)
	index_sum3 += count3


	for x in range(control2,index_sum3):
			array2.append(df['weekly_hosp_admissions'][x])
	
	array2 = [x for x in array2 if math.isnan(x) == False]
	
	if(len(array2)!=0):
		print("Country",end = "      ")
		print("minimum   maximum   average   variation")
		print(df['location'][control2],end = "      ")
		print(round(np.min(array2),3),end = "        ")
		print(round(np.max(array2),3),end = "      ")
		print(round(np.average(array2),3),end = "      ")
		print(round(np.var(array2),3),end = "     ")
		print("\n")
		array2.clear()

	control2 = index_sum3

print("***************************************************************************")

# Q10 What are the average, minimum, maximum and variation values of new tests per day for each country?

print("Q10:\n")

unique_list3 = df['location'].unique()

index_sum3 = 0
control2 = 0
array2 = []

for i in unique_list3:
	count3 = np.count_nonzero(df['location']== i)
	index_sum3 += count3


	for x in range(control2,index_sum3):
		array2.append(df['new_tests'][x])

	array2 = [x for x in array2 if math.isnan(x) == False]
	
	if(len(array2)!=0):
		print("Country",end = "      ")
		print("minimum   maximum   average   variation")
		print(df['location'][control2],end = "      ")
		print(round(np.min(array2),3),end = "        ")
		print(round(np.max(array2),3),end = "      ")
		print(round(np.average(array2),3),end = "      ")
		print(round(np.var(array2),3),end = "     ")
		print("\n")
		array2.clear()

	control2 = index_sum3

print("***************************************************************************")

#Q11 How many tests are conducted in total for each country so far?

print("Q11:\n")

unique_list = df['location'].unique()

index_sum = 0
cntrl = 0

for i in unique_list:
	check = 1
	count = np.count_nonzero(df['location']== i)
	index_sum += count
	print("Country: ",df['location'][index_sum-1])

	for x in range(cntrl,index_sum):
		if(check == count):
			print("Couldn't found a valid total tests are conducted data\n")
			break

		if(not np.isnan(df['total_tests'][index_sum-check])):
			print("Total tests are conducted: ",df['total_tests'][index_sum-check])
			print("\n")
			break

		else:
			check+=1
		cntrl = count


print("***************************************************************************")

# Q12 What are the average, minimum, maximum and variation values of the positive rates of the tests for each
#country?

print("Q12\n")
unique_list3 = df['location'].unique()

index_sum3 = 0
control2 = 0
array2 = []

for i in unique_list3:
	count3 = np.count_nonzero(df['location']== i)
	index_sum3 += count3


	for x in range(control2,index_sum3):
			array2.append(df['positive_rate'][x])
	
	array2 = [x for x in array2 if math.isnan(x) == False]
	
	if(len(array2)!=0):
		print("Country",end = "      ")
		print("minimum   maximum   average   variation")
		print(df['location'][control2],end = "      ")
		print(round(np.min(array2),3),end = "        ")
		print(round(np.max(array2),3),end = "      ")
		print(round(np.average(array2),3),end = "      ")
		print(round(np.var(array2),3),end = "     ")
		print("\n")
		array2.clear()

	control2 = index_sum3

print("***************************************************************************")

#Q13 What are the average, minimum, maximum and variation values of the tests per case for each country?

print("Q13\n")

unique_list3 = df['location'].unique()

index_sum3 = 0
control2 = 0
array2 = []

for i in unique_list3:
	count3 = np.count_nonzero(df['location']== i)
	index_sum3 += count3


	for x in range(control2,index_sum3):
			array2.append(df['tests_per_case'][x])
	
	array2 = [x for x in array2 if math.isnan(x) == False]
	
	if(len(array2)!=0):
		print("Country",end = "      ")
		print("minimum   maximum   average   variation")
		print(df['location'][control2],end = "      ")
		print(round(np.min(array2),3),end = "        ")
		print(round(np.max(array2),3),end = "      ")
		print(round(np.average(array2),3),end = "      ")
		print(round(np.var(array2),3),end = "     ")
		print("\n")
		array2.clear()

	control2 = index_sum3


print("***************************************************************************")
#Q14 How many people are vaccinated by at least one dose in each country?


print("Q14\n")
unique_list = df['location'].unique()

index_sum = 0
cntrl = 0

for i in unique_list:
	check = 1
	count = np.count_nonzero(df['location']== i)
	index_sum += count
	print("Country: ",df['location'][index_sum-1])

	for x in range(cntrl,index_sum):
		if(check == count):
			print("Couldn't found a valid number for people are vaccinated at least one dose data\n")
			break
		if(not np.isnan(df['people_vaccinated'][index_sum-check])):
			print("Number of people are vaccinated by at least one dose: ",df['people_vaccinated'][index_sum-check])
			print("\n")
			break

		else:
			check+=1
		cntrl = count


print("***************************************************************************")

#Q15 How many people are vaccinated fully in each country?

print("Q15\n")
unique_list = df['location'].unique()

index_sum = 0
cntrl = 0

for i in unique_list:
	check = 1
	count = np.count_nonzero(df['location']== i)
	index_sum += count
	print("Country: ",df['location'][index_sum-1])

	for x in range(cntrl,index_sum):
		if(check == count):
			print("Couldn't found a valid number for people are fully vaccinated data\n")
			break
		if(not np.isnan(df['people_fully_vaccinated'][index_sum-check])):
			print("Number of people are fully vaccinated : ",df['people_fully_vaccinated'][index_sum-check])
			print("\n")
			break

		else:
			check+=1
		cntrl = count


print("***************************************************************************")

#Q16 How many vaccinations are administered in each country so far?

print("Q16")

unique_list = df['location'].unique()

index_sum = 0
cntrl = 0

for i in unique_list:
	check = 1
	count = np.count_nonzero(df['location']== i)
	index_sum += count
	print("Country: ",df['location'][index_sum-1])

	for x in range(cntrl,index_sum):
		if(check == count):
			print("Couldn't found a valid number for number of vaccinations are administered\n")
			break
		if(not np.isnan(df['total_vaccinations'][index_sum-check])):
			print("Number of vaccinations are administered: ",df['total_vaccinations'][index_sum-check])
			print("\n")
			break

		else:
			check+=1
		cntrl = count


print("*****************************************  Q17  *******************************************")
'''
Q17
List information about population, median age, # of people aged 65 older, # of people aged 70 older,
economic performance, death rates due to heart disease, diabetes prevalence, # of female smokers, #
of male smokers, handwashing facilities, hospital beds per thousand people, life expectancy and human
development index.
'''

unique_list = df['location'].unique()

index_sum = 0

for i in unique_list:

	count = np.count_nonzero(df['location']== i)
	index_sum += count

	print("Country",end = "      ")
	print("population |  median age |  # of people aged 65 older | # of people aged 70 older |"  
	 + " economic performance  | death rates due to heart disease | diabetes prevalence | # of female smokers | # of male smokers |"
	  + " handwashing facilities | hospital beds per thousand people | life expectancy | human development index")
	print(df['location'][index_sum-1],end = "      ")
	print(df['population'][index_sum-1],end = "        ")
	print(df['median_age'][index_sum-1],end = "      ")
	print(df['aged_65_older'][index_sum-1],end = "      ")
	print(df['aged_70_older'][index_sum-1],end = "      ")
	
	print(df['gdp_per_capita'][index_sum-1],end = "        ")
	print(df['cardiovasc_death_rate'][index_sum-1],end = "      ")
	print(df['diabetes_prevalence'][index_sum-1],end = "      ")
	print(df['female_smokers'][index_sum-1],end = "      ")


	print(df['male_smokers'][index_sum-1],end = "        ")
	print(df['handwashing_facilities'][index_sum-1],end = "      ")
	print(df['hospital_beds_per_thousand'][index_sum-1],end = "      ")
	print(df['life_expectancy'][index_sum-1],end = "      ")
	print(df['human_development_index'][index_sum-1],end = "      ")

	print("\n")

