class laboratory:
    
    def __init__(self, roomnumber):
        self.number = roomnumber 
        
class technician:
    
    def __init__(self, assigned_lab=None):
        self.assigned= assigned_lab
        
    def assign_lab(self, lab_obj):
        self.assigned = lab_obj

lab_01 = laboratory("302")
mr_cruz = technician()

mr_cruz.assign_lab(lab_01)

print(mr_cruz.assigned.number)
