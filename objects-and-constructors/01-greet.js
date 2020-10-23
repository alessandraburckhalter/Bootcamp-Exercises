function Person(name, email, phone) {
    this.name = name;
    this.email = email;
    this.phone = phone;
}

Person.prototype.greet = function(other) {
    console.log('Hello ' + other.name + ', I am ' + this.name + '!');
};


const people = [
    new Person('Sonny', 'sonny@hotmail.com', '483-485-4948'),
    new Person('Jordan', 'jordan@aol.com', '495-586-3456' )
]

people[0].greet(people[1])
people[1].greet(people[0])

Person.prototype.contact = function() {
    console.log(`${this.name}'s email and phone number are ${this.email}, ${this.phone}`);
};

people.forEach(people => {
    people.contact()
})



