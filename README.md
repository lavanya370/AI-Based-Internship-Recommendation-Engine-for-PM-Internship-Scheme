 AI-Based-Internship-Recommendation-Engine-for-PM-Internship-Scheme
This project helps students find the most suitable internships under the Prime Minister Internship Scheme (PMIS) using Artificial Intelligence and Machine Learning. The system analyzes a student's profile, skills, academic performance, interests, and preferred domain, then recommends the best internship opportunities.



1. Problem Statement:

        
         Students often struggle to find internships that match their skills and career goals. Manual searching is time-consuming and may result in unsuitable applications. An AI-powered system can automatically recommend the most relevant internships.



2. Project Objective:


          =>Recommend suitable internships to students.
          
         =>Match student skills with internship requirements.


         =>Increase internship selection chances.
       
         =>Reduce manual effort in searching internships.


         =>Provide personalized recommendations.



3. Modules:


>Module 1: Student Management

         Student Registration

         Login Authentication

         Profile Creation

         Skill Entry

>Module 2: Internship Management

          Add Internship Details

          Company Information

          Internship Requirements

          Duration & Location Details

>Module 3: Recommendation

          Skill Matching

          Interest Analysis

          Eligibility Checking

          Internship Ranking

>Module 4: AI/ML Prediction Module


          Data Preprocessing

          Feature Selection

          Recommendation Model Training

          Internship Prediction
          

>Module 5: Dashboard & Reports
          
         

          Recommended Internships

          Application Status

          Student Analytics

          Recommendation Reports

4. Technologies Used:


  ×Frontend

         React.js

         HTML

         CSS

         Bootstrap


  ×Backend

       Spring Boot (Java)

       REST APIs


  ×Database

        MySQL

  ×Machine Learning

        Python

        Pandas

        NumPy

        Scikit-learn


5. Database Tables:
    

    Student:

          student_id

          name

          email

          department

          cgpa

          skills


     Internship:

          internship_id

          company_name

          role

          required_skills

          location

          duration
   
      
      Recommendation:

            recommendation_id

            student_id

            internship_id

            match_score

    
      Application:

            application_id

            student_id

            internship_id

            status


6.Use Case Actors:
    
      Student=>

            Register

            Login

            Update Profile

            View Recommendation

            Apply Internship
 
       Admin=>

             Manage Students
 
             Manage Internships

             View Reports

             Monitor Recommendations
 

 7.Working Flow
      


         Student Registration
                ↓
         Profile & Skills Entry
                ↓
         Data Preprocessing
                ↓
         AI Recommendation Model
                ↓
         Internship Matching
                ↓
        Top Recommended Internships
                ↓
        Application Tracking

8.ER Diagram:
  
              


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
     


9.AI Algorithm:
   
        
          
      Cosine Similarity

      Content-Based Filtering

      KNN Recommendation
      



      
