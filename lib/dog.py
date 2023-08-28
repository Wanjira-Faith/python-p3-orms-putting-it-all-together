import sqlite3

CONN = sqlite3.connect('lib/dogs.db')
CURSOR = CONN.cursor()

class Dog:

    all = []

    def __init__(self,name,breed):
        self.id = None
        self.name = name
        self.breed = breed

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS dogs(
              id INTEGER PRIMARY KEY,
              name TEXT,
              breed TEXT
            )
        """
        CURSOR.execute(sql)

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS dogs
        """

        CURSOR.execute(sql)

   
    def save(self):
        sql = """
            INSERT INTO dogs (name,breed)
            VALUES(?, ?) 
        """   

        CURSOR.execute(sql, (self.name, self.breed))
        self.id =CURSOR.lastrowid

    @classmethod
    def create(cls,name, breed):
        dog = Dog(name, breed)
        dog.save()
        return dog
    
    @classmethod
    def new_from_db(cls,row):
        id = row[0]
        name = row[1]
        breed = row[2]
        dog = Dog(name, breed)
        dog.id = id
        return dog
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM dogs
        """
        CURSOR.execute(sql)
        results = CURSOR.fetchall()
        dogs = []
        for row in results:
            dog = cls.new_from_db(row)
            dogs.append(dog)
        cls.all = dogs
        return dogs
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT * FROM dogs WHERE name =?
        """
   
        CURSOR.execute(sql, (name,))
        results = CURSOR.fetchall()

        for row in results:
            dog = cls.new_from_db(row)
            return dog

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM dogs WHERE id =?
        """
        CURSOR.execute(sql, (id,))
        results = CURSOR.fetchall()

        for row in results:
            dog = cls.new_from_db(row)
            return dog
        
    @classmethod
    def find_or_create_by(cls, name,breed):
        sql = """
            SELECT * FROM dogs WHERE name =? AND breed =?
        """
        CURSOR.execute(sql, (name, breed))
        results = CURSOR.fetchone()

        if results:
            return cls.new_from_db(results)
        else:
           sql = """
                INSERT INTO dogs (name,breed)
                  VALUES (?,?)
            """
           
           CURSOR.execute(sql, (name, breed))
           new_dog_id = CURSOR.lastrowid

           new_dog = cls(name, breed)
           new_dog.id = new_dog_id
           return new_dog
        
    @classmethod
    def update(cls, id, new_name):
        sql = """
            UPDATE dogs SET name =? WHERE id =?
        """
        CURSOR.execute(sql, (new_name, id))
        CONN.commit()
       
       

            

        


        

        
  
        
        
   
    


    


        

    
    
