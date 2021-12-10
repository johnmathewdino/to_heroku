from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)

    roles = (
        ('1','Dean'),
        ('2', 'Capstone Professor'),
        ('3', 'Faculty'),
        ('4', 'Student'),
    )
    role = models.CharField(max_length=100, choices=roles, default="3")
    image = models.ImageField(upload_to="profiles/",default="profiles/user.png")
    group_name = models.CharField(default="None", null=True, max_length=250)
    group_id = models.CharField(max_length=100, null=True, blank= True, default ="")
    mem1 = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="userprofile_mem1", null=True, blank=True)
    mem2 = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="userprofile_mem2", null=True, blank=True)
    mem3 = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="userprofile_mem3", null=True, blank=True    )
    mem4 = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="userprofile_mem4", null=True, blank=True)
    mem1_fn = models.CharField(max_length=1000, null=True, blank=True, default="")
    mem1_ln = models.CharField(max_length=1000, null=True, blank=True, default="")
    mem1_email = models.CharField(max_length=1000, null=True,  blank=True, default="")
    mem2_fn = models.CharField(max_length=1000, null=True,  blank=True, default="")
    mem2_ln = models.CharField(max_length=1000, null=True,  blank=True, default="")
    mem2_email = models.CharField(max_length=1000, null=True, blank=True, default="")
    mem3_fn = models.CharField(max_length=1000, null=True,  blank=True, default="")
    mem3_ln = models.CharField(max_length=1000, null=True,  blank=True, default="")
    mem3_email = models.CharField(max_length=1000, null=True, blank=True, default="")
    mem4_fn = models.CharField(max_length=1000, null=True,  blank=True, default="")
    mem4_ln = models.CharField(max_length=1000, null=True,  blank=True, default="")
    mem4_email = models.CharField(max_length=1000, null=True,  blank=True, default="")
    # MAKE FOREIGN KEY
    group_adviser = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,default="", related_name="adviser")
    group_title = models.CharField(blank=True, default="", max_length=250, null=True)
    group_panel_1 = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,  blank=True, default="", related_name="panel1")
    group_panel_2 =  models.ForeignKey(User, on_delete=models.SET_NULL, null=True,blank=True, default="", related_name="panel2")
    group_panel_3 =  models.ForeignKey(User, on_delete=models.SET_NULL, null=True,blank=True, default="", related_name="panel3")







    def __str__(self):
        return self.user.get_full_name()

    def deleteUser(sender, instance, **kwargs):
        user = instance.user
        if user:
            user.delete()



