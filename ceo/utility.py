from labor.models import Labor

def register_labor(applicant, pay=33000, post=None):

    try:
        obj = Labor(
        date_of_birth = applicant.dob,
        user = applicant.user,
        first_name = applicant.first_name,
        last_name=applicant.last_name,
        cnic = applicant.cnic,
        phone = applicant.phone,
        gender = applicant.gender,
        address = applicant.address,
        basic_pay = pay,
        post = post
        )
        obj.save()
        return obj
    except Exception as e:
        print(f'unable to save labor, due to: {e}')
        return None

