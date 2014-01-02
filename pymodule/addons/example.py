from pyetw import Addon

#Get Started with Pyet2 :)
#You can define several Addons in one file (group), each addon is represented by a class inherited from pyetw.Addon

class ExampleAddon(Addon):
    group="example" #<--- The name of the file (group) where your addon is defined. (required)
    name= "ExampleAddon"# <---  Set the name you like (excluding 'Core','Main' and 'ExampleAddon'). 
                        #       Be careful to not give the same name twice. (required) 

    def __init__(self):
        Addon.__init__(self)# <--- required if overloading __init__()
        self.call.gPrint("Hello World\n")#<------ Access to ET functions through self.call .
	
    #redefine which event you want to trigger
    def GameConsoleCommand(self):
        if self.call.argv(0) == "getkey":
            info = self.call.GetConfigStr(int(self.call.argv(1)))
            key = self.call.argv(2)

            if info:
                print "\nFound ConfigString !! : \n" + info
                if key:
                    value = self.tools.GetValueForKey(info, key) #Useful tools like (Get,Set)ValueForKey can be found in self.tools .
                    if value:
                        print "\nValue in configstring for key %s is :" %key
                        print value
                    else:
                        print "\nkey does not exist in configstring"     
            else:
                print "ConfigString is empty :/"



inst = ExampleAddon()#required for each addon, name of instance does not matter.

from pyetw import Client

class Example2(Addon):

    """
    How to use the pywet.Client class
    """
    group="example"
    name = "Example2"

    client_manager = Client()

    def ClientUserInfoChanged(self, client):
        """
        This function reverse the player name
        """
        cl = self.client_manager.get_client(client)
        
        actual_name = cl["name"]
        new_name = actual_name[::-1] #reverse the string
        cl["name"] = new_name #update userinfo

        #short version : cl["name"] = cl_["name"][::-1]

inst2 = Example2()	
        
        



