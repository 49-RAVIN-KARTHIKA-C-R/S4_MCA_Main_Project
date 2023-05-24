from django.db import models


class login(models.Model):
    user_name=models.CharField(max_length=100)
    password=models.CharField(max_length=90)
    type=models.CharField(max_length=50)


class program(models.Model):
    program=models.CharField(max_length=100)
    guest=models.CharField(max_length=100)
    date=models.DateField()
    time=models.TimeField()
    photo = models.FileField()

class committee(models.Model):
    login_id=models.ForeignKey(login,on_delete=models.CASCADE)
    committee_name=models.CharField(max_length=100)
    president = models.CharField(max_length=100)
    secretary = models.CharField(max_length=100)
    no_members=models.IntegerField()
    phone=models.BigIntegerField()
    email=models.CharField(max_length=100)


class committe_program(models.Model):
    committee_id=models.ForeignKey(committee, on_delete=models.CASCADE)
    program=models.CharField(max_length=100)
    venue=models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()



class members(models.Model):
    login_id = models.ForeignKey(login, on_delete=models.CASCADE)
    committee_id=models.ForeignKey(committee, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    house_name = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pin = models.BigIntegerField()
    phone = models.BigIntegerField()
    aadhar_number = models.BigIntegerField()
    email = models.CharField(max_length=100)
    photo = models.FileField()




class user(models.Model):
    login_id=models.ForeignKey(login,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    fathers_name = models.CharField(max_length=100)
    house_name=models.CharField(max_length=100)
    street=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    pin=models.IntegerField()
    aadhar_number = models.BigIntegerField()
    phone=models.BigIntegerField()
    email=models.CharField(max_length=100)
    photo = models.FileField()



class auditorium(models.Model):
    auditorium_name=models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    details = models.CharField(max_length=100)
    phone=models.BigIntegerField()
    seats = models.BigIntegerField()
    charge = models.BigIntegerField()
    advance_charge=models.BigIntegerField()
    photo= models.FileField()



class auditorium_booking(models.Model):
    user_id=models.ForeignKey(user,on_delete=models.CASCADE)
    type=models.CharField(max_length=100)
    details=models.CharField(max_length=100)
    date=models.DateField()
    generator = models.CharField(max_length=100)
    status=models.CharField(max_length=100)

class chitti(models.Model):

    type=models.CharField(max_length=100)
    details=models.CharField(max_length=100)
    no_members=models.BigIntegerField()
    duration=models.IntegerField()
    winning_amounts=models.BigIntegerField()
    chitti_amount=models.BigIntegerField()
    date=models.DateField()
    status=models.CharField(max_length=100)
    committee=models.ForeignKey(committee, on_delete=models.CASCADE)




class chitti_details(models.Model):
    chitti_id=models.ForeignKey(chitti,on_delete=models.CASCADE)
    member_id=models.ForeignKey(members,on_delete=models.CASCADE)
    status=models.CharField(max_length=100)
    date=models.DateField()




class chitti_payment(models.Model):
    details_id=models.ForeignKey(chitti_details,on_delete=models.CASCADE)
    date=models.DateField()
    status=models.CharField(max_length=100)

class auditorium_payment(models.Model):
    user_id=models.ForeignKey(user,on_delete=models.CASCADE)
    current_date = models.DateField()
    status = models.CharField(max_length=100)
    booking_date=models.DateField()


class winner(models.Model):
    member_id = models.ForeignKey(members, on_delete=models.CASCADE)
    date=models.DateField()
    chitti_id=models.ForeignKey(chitti,on_delete=models.CASCADE)


# class fine(models.Model):
#     details_id = models.ForeignKey(chitti_details, on_delete=models.CASCADE)
#     fine=models.IntegerField()


class videos(models.Model):
    subject=models.CharField(max_length=100)
    video=models.FileField()
    date_time=models.DateTimeField()

class bank(models.Model):
    bank_name=models.CharField(max_length=100)
    ifsc=models.CharField(max_length=100)
    pin=models.BigIntegerField()
    acc_no=models.BigIntegerField()
    amount=models.BigIntegerField()




# Create your models here.
