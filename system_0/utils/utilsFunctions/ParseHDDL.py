'''
Description: 	Parse the HDDL file				
				Based on https://github.com/tojo2k/pysddl/blob/master/sddl.py/sddl.py, SDDL strings example: D:(A;;CCLCSWLOCRRC;;;AU)(A;;CCLCSWRPLOCRRC;;;PU)
Author: Gricel Vazquez
Last update: 03/10/2020




  


'''




import re
#from win32security import LookupAccountSid,GetBinarySid



text = """
define (domain hospital)
	(:types location robot capability)
	(:types medicalrobot grasprobot - robot) ***
	(:types c1 c2 c3 c4 - location) ***
	(:types measureTemperature measurePressure - capability)
	(:predicates
		(hascapability ?r - robot ?c - capability)
		(at ?r - robot ?l - location)
	)
	

	(:task vitalParameter_Temp_Blood :parameters (?r - robot ?ld - location))
	(:method vitalParameter_Temp_Blood-m
		:parameters (?r - robot ?c1 ?c2 - capability ?ld - location)
		:task (vitalParameter_Temp_Blood ?r ?ld)
		:subtasks(and	***This tasks are not in order as this is assigned later by alloy, move is not needed either
			(measuringTemperature ?r ?c1 ?ld)
			(measuringBloodpressure ?r ?c2 ?ld)
		)
	)

	(:task vitalParameter_Temp :parameters (?r - robot ?ld - location))
	(:method vitalParameter_Temp-m
		:parameters (?r - robot ?c - capability ?ld - location)
		:task (vitalParameter_Temp ?r ?ld)
		:subtasks(and
			(measuringTemperature ?r ?c ?ld)
		)
	)

	(:task vitalParameter_Blood :parameters (?r - robot ?ld - location))
	(:method vitalParameter_Blood-m
		:parameters (?r - robot ?c - capability ?ld - location)
		:task (vitalParameter_Blood ?r ?ld)
		:subtasks(and
			(measuringBloodpressure ?r ?c ?ld)
		)
	)

	(:task moveObject :parameters (?r1 ?r2 - robot ?ls ?ld - location))
	(:method moveObject-m
		:parameters (?r1 ?r2 - robot ?ls ?ld - location c - capability)
		:task (moveObject ?r1 r2? ?c ?ls ?ld)
		:subtasks(and
			(pickObject1 ?r1 ?r2 ?c ?ls)
			(leaveObject ?r1 ?r2 ?c ?ld)
		)
	)

	)

	
		
		
		(medicalrobot ?r)
		(cleanerrobot ?r)
	)

	
	)

	(:method clean-room-m
		:parameters (?r1 ?r2 - robot ?l - location)
		:task (CleanRoom ?r1 ?r2 ?l)
		:ordered-subtasks(and
			(cleaning ?r1 ?r2 ?l)
		)
	)

	



	(:task moveObject :parameters (?r1 ?r2 - robot ?ld - location))


	(:action measuring-temperature
		:parameters (?r - robot ?c1 - capability ?l - location)
		:precondition (and 
			(hascapability ?r ?c)
			(at ?r ?l))
		:effect ()
		:reliability (rtemp)
	)

	(:action measuring-bloodpressure
		:parameters (?r - robot ?c - capability)
		:precondition (and 
			(hascapability ?r ?c)
			(at ?r ?l))
		:effect ()
		:reliability (rblood)
	)

	(:action cleaning
		:parameters (?r1 ?r2 - robot ?l - location)
		:precondition (and 
			(at ?r1 ?l)
			(at ?r2 ?l))
		:effect ()
		:reliability (rclean)
	)

	(:action move
		:parameters (?r - robot ?l1 ?l2 - location)
		:precondition (at ?r ?l1)
		:effect (and
			(not (at ?r ?l1))
			(at ?r ?l2)
			(rewardchange increase (time) (calc-time ?r ?l1 ?l2)))
		:reliability (relMove)
	)
)

"""




# Remove new line
text = text.replace('\n','')

#
# define problem Pattern

pattern = re.findall(r'\(:action'  ,  text)
#print(pattern)



def get_all_in_parens(text):
    in_parens = []
    n = "has something to substitute"       
    while n:
        text, n = re.subn(r'\(([^()]*)\)', # match flat expression in parens
                          lambda m: in_parens.append(m.group(1)) or '', text)
    return in_parens

print(get_all_in_parens(text))
"""
problem = re.compile(r'reliability')
res = problem.match(text)

result = re.match(r'(?:action{1})*', text)

print(res)
print(result)


re_valid_string = re.compile('^[ADO][ADLU]?\\:\\(.*\\)$')

pattern = '^[(:action]'
test_string = 'absyss'


pattern = '^(:action '
pattern = '(:action ).*\.( )|))$'



'(ftp|http):// .*\.(jpg|png)$'

result = re.split(r'%s'.format(pattern), text)


pattern = '^(define (domain '
test_string = text
result = re.match(pattern, test_string)



if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")	


SDDL_TYPE = {'O': 'Owner',
             'G': 'Group',
             'D': 'DACL',
             'S': 'SACL'}

"""
