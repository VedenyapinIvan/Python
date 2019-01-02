# pip3 install py-postgresql
import postgresql

with postgresql.open('pq://postgres:admin@localhost:5432/MSED') as msed:
    count = (msed.query('select count(*) from prg'))[0][0]

    stack = 0
    rehabilitation = 0  # медицинская реабилитация, rhb_type id = 2
    surgery = 0  # реконструктивная хирургия, rhb_type id = 3
    prosthetics = 0  # протезирование, rhb_type id = 4
    while stack < count:
        patients = msed.query('select cfile from prg order by id limit $1 offset $2', 100, stack)
        for person in patients:
            file = person['cfile']
            if ('<IsForChild>false</IsForChild>' in file) and ('<IsFirst>false</IsFirst>' in file):
                with postgresql.open('pq://postgres:admin@localhost:5432/MSE') as mse:

                    # TODO use this for auto parsing
                    # rehabilitation += (mse.query('select count(*) from prg_rhb where prgid=$1 and resid=1 and typeid=2', person['id']))[0][0]
                    # surgery += (mse.query('select count(*) from prg_rhb where prgid=$1 and resid=1 and typeid=3', person['id']))[0][0]
                    # prosthetics += (mse.query('select count(*) from prg_rhb where prgid=$1 and resid=1 and typeid=4', person['id']))[0][0]

                    # TODO usi this for unique parsing
                    actions = mse.query('select typeid from prg_rhb where prgid=$1 and resid=1', person['id'])
                    for act in actions:
                        if act['typeid'] == 2:
                            rehabilitation += 1
                        elif act['typeid'] == 3:
                            surgery += 1
                        elif act['typeid'] == 4:
                            prosthetics += 1

                # print("find id={} rehabilitation={} surgery={} prosthetics={}".format(person['id'], rehabilitation, surgery, prosthetics))

        stack += 100;
    print('all rehabilitation={} surgery={} prosthetics={}'.format(rehabilitation, surgery, prosthetics))