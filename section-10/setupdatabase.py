from basic import db, Puppy

db.create_all()

sam = Puppy(name='Sammy', age=3)
frank = Puppy(name='Frankie', age=4)

print(sam.id)
print(frank.id)

db.session.add_all([sam, frank])

db.session.commit()

print(sam.id)
print(frank.id)