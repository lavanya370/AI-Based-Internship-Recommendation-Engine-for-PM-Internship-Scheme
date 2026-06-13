Students often find it difficult to identify internships that match their skills, interests, and qualifications. Manual searching through numerous internship opportunities is time-consuming and inefficient. This project uses Artificial Intelligence to analyze student profiles and recommend suitable internships under the PM Internship Scheme. The system helps students find relevant opportunities quickly and accurately.
Problem Statement:
     Students often struggle to find internships that match their skills, academic background, and interests. The proposed AI-based recommendation engine aims to provide personalized internship suggestions under the PM Internship Scheme, improving internship opportunities and career development.
Project Objectives
 1.Collect student profile information
	2.Analyze skills and interests using AI.
	3.Recommend suitable internships.
	4.Provide eligibility matching.
	5.Improve internship selection efficiency.
	6.Track internship applications.
Module List:
 Module 1: Student Management
	  Student Registration
   Login
   Profile Management
 Module 2: Internship Management
	  Add Internship Details
   Update Internship Information
   View Available Internships
	Module 3: Resume & Skill Analysis
	  Resume Upload
   Skill Extraction
   Interest Identification
	Module 4: AI Recommendation Engine
	  Profile Analysis
   Skill Matching
   Internship Recommendation
   Match Score Generation
Module 5: Application Tracking
   Apply for Internship
   View Application Status
   Application History
Module 6: Admin Management
   Manage Students
   Manage Internships
   Generate Reports
   Monitor Applications
Table List:
  1. Student Table
  2. Admin Table
  3. Internship Table
  4. Skills Table
  5. Recommendation Table
  6. Application Table
ER Diagram:
  
              


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
 Technologies Used
    Frontend
       HTML
       CSS
       Bootstrap
     JavaScript
   Backend
     Python
     Flask
  Database
     MySQL
  AI/ML
    Pandas
    NumPy
    scikit-Learn
AI Algorithm:     
      Cosine Similarity,Content-Based Filtering,
KNN Recommendation
Benefits
   Personalized internship recommendations.
   Faster internship discovery.
   Better skill-to-job matching.
   Improved internship selection rate.
   Supports career growth and skill development.
   Helps students make informed career decisions
      



      
