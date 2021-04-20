SSD-Assignment 3b
=================
--> Each subsection contains three bullet points. 
--> First point corresponds to description or assumptions made for the respective question.
--> The second point mentions the changes made from previos version and its explaination. 95 additions and 60 deletions have been made from previous version
--> The Third point corresponds to input format.
--> Fourth point corresponds to output format.
### Git Repo Link - 
`https://github.com/AnchalSoni512/SSD_Assignment_3a/tree/partB`
### Q1
* python program to find common leader of any two employees in an organization.
* changes made are mentioned as follows
> imported functool module
> deleted line 6-15
> line no 8- change in function parameter
> deleted line 29 to 55
> added lines fron 19 - 59 for making code generic.
> Implemented input error handling. Used lambda(), set and reduce to get list of common leaders. Printed the leader and levels in required format using for loop.
* It reads a json file `org.json` for the informatio about the organization and user can input `any three to five employees` Emp No.
* The output is common leader (Emp ID) along with the level of the leader from both employee.
### Q2
* python program to find difference between given dates. No date time library has been used.
* changes made are mentioned as follows
> imported sys module to read command line arguments
> added lines 6 to 21 and handled command line input
> removed unneccesary comments
> converted some lines of code to make it modular and reusable.
* User needs to provide a command line arguments if any one/both the date formats are `'.','-' or '/'` seperated stating the type of date format. For the date format  containing word or first three letters of the month, no command line input is to be given.
Input file `date_calculator.txt` should be in following `5` formats with `two rows`:
valid date formats
`10th September, 2020`
`1st September, 2020`
`10th Sep, 2020`
`dd/mm/yyyy`
`dd-mm-yyyy`
`dd.mm.yyyy`
`mm/dd/yyyy`
`mm-dd-yyyy`
`mm.dd.yyyy`
* Output file `output.txt` will have output in number of days

### Q3
* Program searchs for all free slots for the given two employees and reserves the first available common slot. No date time library has been used.
* Time slots to be taken as `9:00AM` instead of `09:00AM`
* Two text files `Employee1.txt` and `Employee2.txt` containing the busy slots of each employee in a dictionary format.
Slot duration to be inputted by the user during run time.
* Output file contains the following,
 --> All Available slots before blocking the slot,
 --> Time of the blocked slot for the both employees.If no common slot available, then prints no slot available.
