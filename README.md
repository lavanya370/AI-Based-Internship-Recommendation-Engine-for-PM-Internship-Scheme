 AI-Based-Internship-Recommendation-Engine-for-PM-Internship-Scheme
This project helps students find the most suitable internships under the Prime Minister Internship Scheme (PMIS) using Artificial Intelligence and Machine Learning. The system analyzes a student's profile, skills, academic performance, interests, and preferred domain, then recommends the best internship opportunity
 
Problem Statement

Many students struggle to identify internships that match their skills and interests. Existing internship portals provide numerous opportunities, making it difficult to choose the right one. This project solves the problem by using Artificial Intelligence to provide personalized internship recommendations.
Objectives
Recommend suitable internships based on student profiles.
Match student skills with internship requirements.
Reduce manual effort in internship searching.
Improve internship selection accuracy.
Support students participating in the PM Internship Scheme.

Modules

1. Student Module

Student Registration
Login
Profile Management
Skills and Interest Management
2. Internship Module
Internship Listings
Company Details
Internship Requirements

3. Recommendation Module

Skill Matching
Internship Ranking
Match Score Calculation

4. Application Module

Apply for Internships
Track Application Status

5. Admin Module

Manage Students
Manage Internships
Generate Reports

6. Support Module

Feedback System
Query Handling
Ticket Management

Input Parameters
The recommendation system uses the following inputs:

Department,
CGPA,
Skills,
Certifications,
Projects,
Preferred Domain,
Preferred Location,
Internship Experience,
Resume Information.

Process Flow

Student registers and logs into the system.
Student enters profile details and skills.
Internship data is stored in the database.
AI algorithm compares student skills with internship requirements.
Match scores are calculated.
Top-ranked internships are recommended.
Student applies for preferred internships.
Application status is tracked.

Technology Stack

Frontend

React.js
HTML
CSS
Bootstrap
JavaScript

Backend

Spring Boot
Java
REST API

Database

MySQL
AI/ML
Python
Pandas
NumPy
Scikit-Learn
Database Tables

Student

student_id
name
email
department
cgpa
skills

Internship

internship_id
company_name
role
required_skills
location

Recommendation

recommendation_id
student_id
internship_id
match_score
Application
application_id
student_id
internship_id

status
Admin
admin_id
username
password

7.ER Diagram:
  
              


           |department     |

           | cgpa           |

           | skills         |

            +----------------+

                  |

                  | 1

                  |

                  | M

          +-------------------+

          | APPLICATION       |

          +-------------------+

          | application_id(PK)|

          | student_id(FK)    |

          | internship_id(FK) |

          | status            |

          +-------------------+

                |

                | M

                |

                | 1
 
          +----------------+

          | INTERNSHIP     |

          +----------------+

          | internship_id  |

          | company_name   |

          | role           |

          | required_skill |

          | duration       |

          | location       |

          +----------------+


               |

               | 1

               |

               | M

       +----------------------+

       | RECOMMENDATION       |

      +----------------------+

      | recommendation_id(PK)|

      | student_id(FK)       |

      | internship_id(FK)    |

      | match_score          |

      +----------------------+
     


8.AI Algorithm:     
      Cosine Similarity,Content-Based Filtering,
KNN Recommendation
Benefits
Personalized internship recommendations.
Faster internship discovery.
Better skill-to-job matching.
Improved internship selection rate.
Supports career growth and skill development.
Helps students make informed career decisions
      



      
