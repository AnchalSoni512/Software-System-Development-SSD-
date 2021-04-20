SSD-Assignment 3a
=================
--> Each subsection contains three bullet points. 
--> First point corresponds to description or assumptions made for the respective question.
--> The second point corresponds to input format.
--> Third point corresponds to output format.

### Q1
* python program to find common leader of any two employees in an organization.
* It reads a json file `org.json` for the informatio about the organization and user can input any two employees’ Emp No.
* The output is common leader (Emp ID) along with the level of the leader from both employee.
### Q2
* python program to find difference between given dates. No date time library has been used.
* Input file `date_calculator.txt` should be in following `5` formats with `two rows`:
valid date formats
`10th September, 2020`
`1st September, 2020`
`10th Sep, 2020`
`DD/MM/YYYY`
`DD-MM-YYYY`
`DD.MM.YYYY`
* Output file `output.txt` will have output in number of days

### Q3
* Program searchs for all free slots for the given two employees and reserves the first available common slot. No date time library has been used.
* Time slots to be taken as `9:00AM` instead of `09:00AM`
* Two text files `Employee1.txt` and `Employee2.txt` containing the busy slots of each employee in a dictionary format.
Slot duration to be inputted by the user during run time.
* Output file contains the following,
 --> All Available slots before blocking the slot,
 --> Time of the blocked slot for the both employees.If no common slot available, then prints no slot available.

