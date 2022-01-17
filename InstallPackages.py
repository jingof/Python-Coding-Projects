"""
Computers download, install and use packages(softwares) with different versions, in this task 
we want to find out how which packages are downloaded at the end of an instruction. There are two operations;
    "add"     : This adds a package to a group of packages to be downloaded.
    "install" : This downloads and installs all the pending packages in the group.

Instructions are in two formats
       1. ["add","express","1.1"] where "add" is the instructions
                                      "express" is the package name
                                      "1.1" is the version of the package
        2. ["install"]

When a package has not been installed yet and the same package with a different version is added, the initial package should be replaced.

When a package is already installed and the same package with a different version is added, the initial package should not be replaced.

The solution should return a list of all installed packages in the format ["package-version","package-version","package-version"]

The list must be sorted in ascending order of the package name and the version. If there are two packages
 ["express-10.1", "express-2.0"] in the list. The sorted list should be ["express-2.0", "express-10.1"].

Example:
    Given instructions below.
    [ ["add", "express", "1.1"], 
      ["add", "async", "1.0"], 
      ["add", "express", "10.0"], 
      ["install"], 
      ["add", "express", "2.2"], 
      ["install"]  ]

      1. The "express" package with version "1.1" is added to the pending group.
      2. The "async" package with version "1.0" is added to the pending group.
      3. The "express" package with version "10.0" replaces the "express" package with version "1.1" because no package has been installed.
      4. The two packages are downloaded and installed.
      5. The "express" package with version "2.2" is added to the pending group.
      6. The "express" package is downloaded and installed, in total there are 3 packages installed.
    
    The result of the above should be ["async-1.0","express-2.2","express-10.0"]
"""

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
                if package.installed == False:
                    package.installed = True
     
    packages =sortList(packages)
    lista = []
    for package in packages:
        phrase = package.name+"-"+package.version
        lista.append(phrase)  
    return lista
        
    


operations=[["add", "express", "1.1"], ["add", "async", "1.0"], ["add", "express", "10.0"], ["install"], ["add", "express", "2.2"], ["install"]]
print(solution(operations))
