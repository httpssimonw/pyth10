class Course:
    def __init__(self, title, instructor, duration):
        self.title = title
        self.instructor = instructor
        self.duration = duration

    def get_info(self):
        return f"Course: {self.title}\nInstructor: {self.instructor}\nDuration: {self.duration} hours"
    
    def __str__(self):
        return self.get_info()



class OnlineCourse(Course):
    def __init__(self, title, instructor, duration, platform):
        super().__init__(title, instructor, duration)
        self.platform = platform

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}\nPlatform: {self.platform}"
    
    def __str__(self):
        return self.get_info()



class CertificateOnlineCourse(OnlineCourse):
    def __init__(self, title, instructor, duration, platform, certificate):
        super().__init__(title, instructor, duration, platform)
        self.certificate = certificate

    def get_info(self):
        base_info = super().get_info()
        cert_status = "Да" if self.certificate else "Нет"
        return f"{base_info}\nCertificate Available: {cert_status}"
    
    def __str__(self):
        return self.get_info()


course = Course("Python Basics", "Асема", 16)
online_course = OnlineCourse("Python Advanced", "Адель", 20, "Udemy")
cert_course = CertificateOnlineCourse("Data Science with Python", "Eldana", 19, "Coursera", True)

print(course)
print(online_course)
print(cert_course)







# class Python:
#     def expl(self):
#         return "Python идет"
    
#     def greeting(self):
#         return 'Hello! I am Python'

# class JS:
#     def expl(self):
#         return "JS идет"
    
#     def greeting(self):
#         return 'Hello! I am JavaScript'

# # Функция для вызова greeting и отображения результата
# def introduce_course(course):
#     print(course.greeting())

# python = Python() 
# js = JS() 

# introduce_course(python) 
# introduce_course(js)
