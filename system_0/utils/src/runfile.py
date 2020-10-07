

from system_0.config import settings

import os

settings.HDDL_TO_JAVA_FILE
settings.DSL_TO_JAVA_FILE 
settings.JAVA_TO_ALLOY_FILE


javafiles = 'javac Allocate.java Alloy.java Capability.java CompositeTask.java java2alloy.java Location.java Plan.java Robot.java Task.java'

os.system('python '+settings.HDDL_TO_JAVA_FILE)
time.sleep(3)

os.system('cd '+settings.JAVA_FILES_PATH ,'javac '+javafiles)
time.sleep(3)


os.system('cd '+settings.JAVA_FILES_PATH ,'java '+'java2alloy.class')
time.sleep(3)

# run java file to create Alloy instances

# run code to generate augmented robot dabases

# run code to generate PRISM file from augmented robot dabases


#DONE: multiple PRISM outputs
#NEXT step: select PRISM model with less cost