class Packages:
    def __init__(self, name = "",version=""):
        self.name = name
        self.version = version
        self.installed = False
        
    def __str__(self):
        return f"{self.name} with version is {self.version}, and installed = {self.installed}"

#### END OF CLASS ####


def sortList(packages):
    i = 0
    j = 0
    while(i < len(packages)-1):
        package1 = packages[i]     
        changed = False
        j = i+1
        while(j < len(packages)):
            package2 = packages[j]         
            if package1.name == package2.name and float(package2.version) < float(package1.version):
                temp1Name = str(package1.name)
                temp1Vers = str(package1.version)
                temp2Name = str(package2.name)
                temp2Vers = str(package2.version)
                
                packages[i].name = temp2Name
                packages[i].version = temp2Vers
                packages[j].name = temp1Name
                packages[j].version = temp1Vers  
                changed = True

            elif package1.name > package2.name:
                
                temp1Name = str(package1.name)
                temp1Vers = str(package1.version)
                temp2Name = str(package2.name)
                temp2Vers = str(package2.version)
                
                packages[i].name = temp2Name
                packages[i].version = temp2Vers
                packages[j].name = temp1Name
                packages[j].version = temp1Vers
                changed = True
                
            j+=1

        if changed == True:
            j = 0
            changed = False
        else:
            i+=1

    return packages

def solution(operations):
    packages = []
    
    for operation in operations:
        added = False
        if operation[0] == 'add':
            for package in packages:
                
                if package.name == operation[1] and package.installed == False:
                    package.version = operation[2]
                    added= True
        
            if added == False:    
                p = Packages(operation[1], operation[2])        
                packages.append(p)
        if operation[0] == 'install':
            for package in packages:
                package.installed = True
     
    packages =sortList(packages)
    lista = []
    for package in packages:
        phrase = package.name+"-"+package.version
        lista.append(phrase)  
    return lista
        
    


operations = [["add", "express", "1.1"], ["add", "async", "1.0"], ["add", "express", "10.0"], ["install"], ["add", "express", "2.2"], ["install"]]
print(solution(operations))
