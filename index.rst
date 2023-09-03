<!DOCTYPE html>
<html>
<head>
    <title>Market Research Guide</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    <style>
        /* Basic CSS styling for the two-column layout */
        body {
            font-family: "Open Sans", sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }
        .header {
            background-color: #010b49;
            color: #fff;
            font-size: 14px;
            padding: 20px;
            width: 20%;
            
            
        }
        .project-name {
            flex: 2;
            background-color: #010b49;
            padding: 10px 20px;
            color: #fff;
            font-size: 15px;
            margin-top: px;
            text-align: left;
            margin-bottom: px;
            display: flex;
            align-items: center;  /* left the content horizontally */
        }
        .project-name h1 {
            margin: 0;
            font-size: 32px;
            margin-right: 10px;
        }

        .project-name p {
            font-size: 16px;
            margin: 0   ;
            opacity: 0.8;
        }
        .icon-home {
            margin-right: 10px; /* Add some space between the icon and text */
        }
        .wy-form {
            flex: 1;
            margin-left: 20px;
        }

        .wy-form input[type="text"] {
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 5px;
            width: 100%;
        }

        .container {
            display: flex;
            background-color: #fff;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            overflow: auto; /* Prevent child elements from overflowing */
        
        }

        .navigation {
            flex: .5;
            padding: 30px;
            background-color: #2b2a2d;
            color: #fff;
        }

        .navigation h2 {
            font-size: 20px;
            margin-bottom: px;
            padding-bottom: 10px;
            border-bottom: px solid #fff;
        }

        .navigation ul {
            list-style-type: none;
            padding: 0;
        }

        .navigation li {
            margin-bottom: 10px;
        }

        .navigation a {
            text-decoration: none;
            color: #fff;
        }

        .navigation a:hover {
            color: #230749;
        }

        .explanation {
            flex: 2;
            padding: 20px;
        }
        @media screen and (max-width: 600px) {
      .container {
        padding: 10px;
      }
    }

        .project-name {
            background-color: #010b49;
            padding: 30px;
            color: #fff;
            font-size: 20px;
            margin-bottom: px;
        }
        .image-container {
            flex: 1;
            max-width: 80%;
            margin-left: 20px;
        }

        .image-container img {
            width: 100%;
            max-width: 100%;
            height: auto;
            display: block;
        }

        /* Show the "Overview" section by default */
        .section {
            display: none;
        }

        .section#overview {
            display: block;
        }
    </style>
    <script>
        function searchContent() {
            var searchTerm = document.getElementById("search-input").value.toLowerCase();
            // Perform your search logic here
            // In this example, I'm checking if the search term exists in the overview content
            var overviewContent = document.getElementById("overview").textContent.toLowerCase();
            
            if (overviewContent.includes(searchTerm)) {
                showSection('overview'); // Show the overview section if search term is found
            } else {
                console.log("Search term not found in overview");
            }
        }
        function showSection(sectionId) {
            var sections = document.getElementsByClassName("section");
            for (var i = 0; i < sections.length; i++) {
                sections[i].style.display = "none";
            }
            document.getElementById(sectionId).style.display = "block";
        }
        function showSubSection(subSectionId) {
        var subSection = document.getElementById(subSectionId);
        if (subSection) {
            if (subSection.style.display === 'block') {
                subSection.style.display = 'none';
            } else {
                subSection.style.display = 'block';
            }
        }
    }
    

    function hideSubSection(subSectionId) {
        var subSection = document.getElementById(subSectionId);
        if (subSection) {
            subSection.style.display = 'none';
        }
    }
    </script>
</head>
<body>
    <div class="header">
       
        <div class="project-name">
            <i class="fas fa-home icon-home"></i>
            <h1>Market Research Guide</h1>
            
           
            
        </div>
        <div class="wy-form">
            <input type="text" placeholder="Search..." id="search-input">
            <button onclick="searchContent()">Search</button>
        </div>

    </div>

    <div class="container">
        <div class="navigation">
            <h2>Home</h2>
            <ul>
                <li><a href="javascript:void(0);" onclick="showSection('overview')">Overview</a></li>
                <li><a href="javascript:void(0);" onclick="showSection('methodologies')">Methodologies</a></li>
                <li><a href="javascript:void(0);" onclick="showSection('internal-analysis')">Internal Analysis</a></li>
                <li><a href="javascript:void(0);" onclick="showSection('external-analysis')">External Analysis</a></li>
                <li><a href="javascript:void(0);" onclick="showSection('ethical-considerations')">Ethical Considerations</a></li>
                <li><a href="javascript:void(0);" onclick="showSection('findings')">Present Your Findings</a></li>
                <li><a href="javascript:void(0);" onclick="showSection('recommendations')">Recommendations</a></li>
                <li><a href="javascript:void(0);" onclick="showSection('conclusion')">Conclusion</a></li>
                <li><a href="javascript:void(0);" onclick="showSection('references')">References</a></li>
                <li><a href="javascript:void(0);" onclick="showSection('feedback')">Feedback</a></li>
            </ul>
        </div>
        
        

        <div class="explanation">
            <div class="section" id="overview">
                <p><h1>Welcome to the Market Research Guide</h1>
                <h2>Overview</h2>
    <p>In the fast-changing world of business today, it's really important to make smart decisions to succeed. Market research acts like a helpful guide, showing us the right path by giving us deep insights about industries, target customers, and competitors. Our complete Market Research Guide is here to help you at every step, from figuring out what you want to learn to understanding tricky data trends, and using them to make smart plans.</p>
                    
                    <ul>
                        <li>
    
       <a class="reference internal" href="javascript:void(0);" onclick="showSubSection('introduction')"> Introduction</a>
    
</li>
<li>
    <a class="reference internal" href="javascript:void(0);" onclick="showSubSection('purposes-objectives')">Purposes and Objectives</a>
</li>
<li>
    <a class="reference internal" href="javascript:void(0);" onclick="showSubSection('scope-coverage')">Scope and Coverage</a>
</li> 
<li>
   <a class="reference internal" href="javascript:void(0);" onclick="showSubSection('benefits')">Benefits</a>
</li> 
<li>
    <a class="reference internal" href="javascript:void(0);" onclick="showSubSection('examples')">Examples</a>
</li>
<li>
  <a class="reference internal" href="javascript:void(0);" onclick="showSubSection('acknowledgment')">Acknowledgment</a>
</li>       
<li>
    <a class="reference internal" href="javascript:void(0);" onclick="showSubSection('distribution')">Distribution</a>
</li>       
<li>
    <a class="reference internal" href="javascript:void(0);" onclick="showSubSection('updates')">Updates</a>
</li>       
<li><a class="reference internal" href="javascript:void(0);" onclick="showSubSection('contact-info')">Contact Information</a></li>       
      </ul>

                    <div class="subsection" id="introduction" style="display: none;">
    <h3>Introduction</h3>
    <p>Market research is an organized effort to gather information about target markets and customers.</p>
    <p>A market research guide is a comprehensive and structured resource that provides individuals, businesses, and researchers with detailed instructions, methodologies, and insights to effectively conduct market research.</p>
</div>

<div class="subsection" id="purposes-objectives" style="display: none;">
    <h3>Purposes and Objectives</h3>
    <p> A  the market research guide serves as a valuable resource that offers step-by-step instructions, methodologies, best practices, and insights to guide users through the process of gathering, analyzing, and interpreting data about a specific market, industry, or target audience</p>
    <p>The main objectives of a market research guide includes -</p>

    <img src="Purposeandobject.jpg" alt="Image Description" style="max-width: 80%; height: auto;">
</div>

<div class="subsection" id="scope-coverage" style="display: none;">
    <h3 class="subsection-title">Scope and Coverage</h3>
    <div class="subsection-content">
        <p class="subsection-description">Market research is an industry that overlaps with and is often referred to as the "insights" industry.</p>
        <p class="subsection-description">Key principles that shape the scope and coverage of market research include:</p>
        <ol class="subsection-list">
            <li class="subsection-item">Framing Managerial Anomalies: An anomaly is a puzzle or perplexing situation that market research reports aim to solve.</li>
            <li class="subsection-item">Loading Instruments with Meanings: Observations of commonplace social practices are translated into the marketing ontology.</li>
            <li class="subsection-item">Signposting Prescriptions: Intended readings are guided to reduce interpretive flexibility.</li>
        </ol>
    </div>
</div>

<div class="subsection" id="benefits" style="display: none;">
    <h3>Benefits</h3>
    <div class="subsection-content">
        <p class="subsection-description">
            <strong>Identifying opportunities in Market Research:</strong> Market research helps us identify areas where there's a demand for our products or services, gaps in the market that we can fill, and trends that we can capitalize on.
        </p>
        <p class="subsection-description">
            <strong>Measures business reputation:</strong> Evaluating Company Image and Standing
        </p>
        <p class="subsection-description">
            <strong> Help in minimize risks:</strong> Aiding in risk reduction
        </p>
    </div>
    <img src="Picture2.jpg" alt="benfit daigram" style="max-width: 80%; height: auto;">
</div>
<div class="subsection" id="examples" style="display: none;">
    <h3>Examples</h3>
    <div class="subsection-content">
        <p class="subsection-description">
            <strong>REAL ROBOTICS ( TOPAS )</strong>
        </p>
        <p class="subsection-description">
            <img src="Picture4.jpg" alt="example" style="max-width: 60%;height:auto;">
        </p>
        <p class="subsection-description">
            <strong>Goal:</strong> 100% autonomous field Robots. 
        </p>
        <p class="subsection-description">
        <strong> Objective :</strong><br>
        ☑ To create a software for autonomous lawn mowing robots with the use of digital twins, sensor fusion and intelligent planning and control.<br>
        ☑ Optimizing process by using AI tools such as "WORHP"
        </p>
        <p class="subsection-description">
            <strong>Research and Industry Partners:</strong> Alpha Robotics, Institute for Cognitive Neuroinformatics (CNI) 
        </p>
        <p class="subsection-description">
            <strong>Implications:</strong>
            <p class="subsection-description">
                <strong>1. Product Features -:</strong>Intelligent and efficient lawn mowing.
            </p>
            <p class="subsection-description">
                <strong>2. Market Message  -:</strong>High-performance robot lawn mowers for the care of large green spaces.
            </p>
            <p class="subsection-description">
                <strong>3. User Experience -:</strong>Time optimal,GPS-based localization removes the need for physical boundaries and  minimal user effort.
            </p>
        </p>
        <p class="subsection-description">
            <strong>Conclusion:</strong>Transforming innovative and holistic algorithms from current research in mathematics and computer science for direct application to industry and medium sized companies.
        </p>


    </div>
</div>

<div class="subsection" id="acknowledgment" style="display: none;">
    <h3 class="subsection-title">Acknowledgment</h3>
    <div class="subsection-content">
        <p class="subsection-description">We extend our heartfelt gratitude to the individuals and organizations whose support, expertise, and contributions made the creation of this market research guide possible. Their dedication and insights have greatly enriched the content and value of this resource.</p>
        
        <p class="subsection-description">We would like to thank:</p>
        
        <ul class="subsection-list">
            <li class="subsection-item"> <strong>Praxis Summer Camp Organization: </strong> their time, candid responses, and willingness to share their perspectives, which added depth to our understanding and for giving us an opportunity to be a part of this project.</li>
            <li class="subsection-item"> <strong>Simran Wadhwa, Milin Zhang, and Rajendra Didel:</strong> The driving force behind this guide's creation, who have poured their expertise, passion, and countless hours into crafting a comprehensive and insightful resource.</li>
            <li class="subsection-item"> <strong>Martin Holi:</strong> For their invaluable guidance and expert insights throughout the development of this guide.</li>
            <li class="subsection-item"> <strong>Emmanuel Opoku:</strong> For their diligent research efforts, meticulous review, and valuable feedback that greatly enhanced the accuracy and clarity of this guide.</li>
            <li class="subsection-item"> <strong>TOPAS: </strong> For generously providing access to relevant data and resources, enriching the quality of our research.</li>
        </ul>
        
        <p class="subsection-description">This guide stands as a collective effort, and we are deeply appreciative of everyone who played a role, no matter how big or small.</p>
    </div>
</div>

<div class="subsection" id="distribution" style="display: none;">
    <h3 class="subsection-title">Distribution</h3>
    <div class="subsection-content">
    
        <p>The guide is easily accessible at <a href="https://pscmarketresearch17.github.io/marketresearch17.github.io/">https://pscmarketresearch17.github.io/marketresearch17.github.io/</a></p>

<p>We have created a dedicated feedback form where you can provide detailed feedback on specific sections of the guide, offer suggestions for improvement, and share your overall experience.</p>
<p><a href="https://docs.google.com/forms/d/e/1FAIpQLSfrSBi2DY38fT0dTtVYejOToE_z9iti9PASNXLZDeuef0_WkQ/viewform?usp=sf_link">Feedback Form</a></p>

    </div>
</div>

<div class="subsection" id="updates" style="display: none;">
    <h3 class="subsection-title">Updates</h3>
    <div class="subsection-content">
        <p class="subsection-description">We understand that the effectiveness of the guide relies on its accuracy and relevance. Our commitment to continuous improvement means that we will regularly review and update the content to reflect the latest insights, methodologies, and best practices in the field of market research.</p>
        <p class="subsection-description">Thank you for your interest in the market research guide, and we look forward to keeping you informed about its ongoing evolution.</p>
    </div>
</div>


<div class="subsection" id="contact-info" style="display: none;">
    <h3 class="subsection-title">Contact Information</h3>
        <div class="subsection-content">
            <p class="subsection-description">If you have any questions, feedback, or inquiries related to the market research guide, please don't hesitate to reach out to us.</p>
            <p class="subsection-description">Email : <a href="mailto:pscmarketresearch17@gmail.com">pscmarketresearch17@gmail.com</a></p>
            <p>martin.holi@topas.tech</p>
            <p class="subsection-description">We appreciate your engagement and are committed to providing you with the support you need to make the most of this market research guide.</p>
        </div>
    </div>



            </div>
        
        

            <div class="section" id="methodologies">
                <h2>Methodologies</h2>
                <p>Describe the methodologies used in your market research.</p>
                <p class="subsection-description">
                    <img src="Picture3.jpg" alt="example" style="max-width: 60%;height:auto;">
                </p>
                <ul>
                    <li><a class="reference internal" href="javascript:void(0);" onclick="showSubSection('secondary-research')"> Secondary research</a></li>
                    <li><a class="reference internal" href="javascript:void(0);" onclick="showSubSection('qualitative research')">Qualitative research</a></li>
                    <li><a class="reference internal" href="javascript:void(0);" onclick="showSubSection('quantitative research')">Quantitative research</a></li>                           
                </ul>
                <div class="subsection" id="secondary-research" style="display: none;">
                    <h3>Secondary research</h3>
                    <div class="subsection-content">
                        <p class="subsection-description">Primary data is sourced by the researcher for the specific purpose of addressing the research problem. On the other hand, secondary data is collected for some purpose other than the  problem at hand. In the market research area, secondary data comes from various resources, including information made available by business and government sources, commercial marketing research firms, and computerised databases, etc. 
 
                            Further recommendations for secondary data sources can be found in the Recommendation section of this website.
                            </p>
                    </div>
                </div>
                <div class="subsection" id="qualitative research" style="display: none;">
                    <h3>Qualitative research</h3>
                    <div class="subsection-content">
                        <p class="subsection-description">Information, industry experts, and secondary data may not be sufficient to define the research problem. Sometimes qualitative research must be undertaken to gain a qualitative understanding of the problem and its underlying factors. Qualitative research is unstructured, exploratory in nature, based on small samples, and may utilize popular qualitative techniques such as focus groups, in-depth interviews, and usability tests, etc.
                        </p>
                        <p class="subsection-description">Potential targets for qualitative research include company heads and employees, competing companies, users, public sectors, researchers, associations in the field, etc.
                        </p>
                        <h4>Focus group</h4>
                        <p class="subsection-description">The focus group method is a qualitative research technique used to gather insights and opinions from a small, diverse group of individuals about a specific topic, product, service, or concept. It involves guided discussions led by a trained moderator in a structured and interactive environment.
                        </p>
                        <p class="subsection-description">In the market research area, focus group methods can contribute to Exploratory Research, Concept Testing, Customer Behavior and Decision-Making, Customer Satisfaction and Feedback, etc.
                        </p>
                        <p class="subsection-description">To conduct a focus group, researchers typically follow these steps:</p>
                        <ol class="subsection-description">
                            <li> <strong>Define the Objective:</strong> Clearly outline the research objectives and questions you want to address through the focus group discussions.</li>
                            <li><strong>Recruit Participants:</strong> Select a diverse group of participants who represent your target audience. Participants should have relevant knowledge and experiences related to the topic.</li>
                            <li><strong>Moderation:</strong> A skilled moderator leads the discussion, ensures that all participants have an opportunity to speak, and guides the conversation based on a predefined discussion guide.</li>
                            <li><strong>Data Collection:</strong> Researchers record the discussions, often with audio or video equipment, and take notes on participants' comments, reactions, and interactions.</li>
                            <li><strong>Data Analysis:</strong> Transcribe and analyze the discussion data to identify patterns, themes, and insights relevant to the research objectives.</li>
                            <li><strong>Report and Findings:</strong> Summarize the key findings and insights from the focus group discussions in a report that can inform marketing strategies, product development, and decision-making.</li>
                        </ol>
                        <p class="subsection-description">Template for Focus Group from Hubspot: <a href="https://docs.google.com/document/d/1FNdK5vMU0QnRQBOERYcu8OtTdWuFI26uco_OTcRSQ8c/copy">View Template</a></p>
                        <h4>In-depth Interview</h4>
                        <p class="subsection-description">The interview method is a qualitative research technique that involves direct one-on-one interactions between a researcher and a participant to gather in-depth information, insights, and opinions. Interviews are conducted in a conversational manner, allowing the researcher to probe and explore the participant's thoughts, experiences, and perspectives on a specific topic.</p>
                        <p class="subsection-description">In the market research area, the interview method can contribute to In-depth Consumer Insights, New Product Development, User Experience and Usability Testing, Competitor Analysis, Trend and Market Analysis, etc.</p>
                        <p class="subsection-description">To conduct interviews for market research, follow these steps:</p>
                        <p class="subsection-description">
                            <li><strong>Define Objectives: </strong>Clearly outline the research objectives and the specific topics you want to explore through the interviews.</li>
                            <li><strong>Recruit Participants: </strong>Select a diverse group of participants who represent your target audience and have relevant insights to share.</li>
                            <li><strong>Preparation: </strong>Develop a list of open-ended questions and discussion topics that will guide the interview. Ensure the questions encourage participants to share detailed responses.</li>
                            <li><strong>Conduct Interviews: </strong>Conduct the interviews either in person, over the phone, or via video conferencing. Create a comfortable and relaxed environment that encourages open and honest communication.</li>
                            <li><strong>Data Collection: </strong>Record the interviews, with the participant's consent, and take detailed notes during the conversations.</li>
                            <li><strong>Data Analysis: </strong>Transcribe and analyze the interview data to identify patterns, themes, and insights relevant to the research objectives.</li>
                            <li><strong>Report and Findings:</strong> Summarize the key findings and insights from the interviews in a report that can inform marketing strategies, product development, and decision-making.</li>
                        </p>
                        <p class="subsection-description">More qualitative research methods: Ethnography, Diary studies, Usability tests, etc.</p>
                    </div>
                </div>
                <div class="subsection" id="quantitative research" style="display: none;">
                    <h3>Quantitative research</h3>
                    <div class="subsection-content">
                        <h4>Survey</h4>
                        <p class="subsection-description">The survey method is a research technique used to collect data from a group of individuals by asking them a series of structured questions. Surveys are typically administered through various mediums, such as paper questionnaires, online forms, telephone interviews, or face-to-face interactions.</p>
                        <p class="subsection-description">In the market research area, the survey method can contribute to Customer Satisfaction and Feedback, Product Development, Pricing Research, Advertising and Marketing Campaigns, Brand Perception, etc.</p>
                        <p class="subsection-description">To conduct a survey for market research, follow these steps:</p>
                        <p class="subsection-description">
                            <li><strong>Define Objectives:</strong> Clearly outline the research objectives and the specific topics or questions you want to address through the survey.</li>
                            <li><strong>Design the Survey:</strong> Create a well-structured questionnaire with a mix of closed-ended (multiple choice, rating scales) and open-ended (textual) questions. Ensure the questions are clear, concise, and unbiased.</li>
                            <ul class="subsection-description">
                                <li><a href="https://www.surveymonkey.com/">SurveyMonkey</a>: Offers videos and tutorials on survey design, best practices, and data analysis.</li>
                                <li><a href="https://www.qualtrics.com/uk/?rid=ip&prevsite=en&newsite=uk&geo=DE&geomatch=uk">Qualtrics</a>: Provides videos on survey design, research methodology, and data analysis.</li>
                            </ul>
                            <li><strong>Sampling:</strong> Decide on the target audience for the survey and select a representative sample from that population. The sample size should be statistically valid to ensure accurate results.</li>
                            <li><strong>Data Collection:</strong> Administer the survey using the chosen medium (online, paper, telephone, in-person). Ensure that participants understand the instructions and can easily respond.</li>
                            <li><strong>Data Analysis:</strong> Tabulate and analyze the survey responses. Use statistical tools to identify trends, correlations, and insights.</li>
                            <li><strong>Report and Findings:</strong> Summarize the key findings from the survey in a report that can guide marketing strategies, product development, and decision-making.</li>
                        </p>
                        <p class="subsection-description"><strong>More quantitative research methods:</strong> Data analytics, Eyetracking and biometrics, etc.</p>
                    </div>
                </div>
                

            </div>

    <div class="section" id="internal-analysis">
        <h2>Internal Analysis</h2>
        <div class="subsection-content">
            <p class="subsection-description">Before going into market research and analyzing your buyers and competitors, you first need to understand your own organization: its structure, potential, advantages, and innovations. This section helps you go through the key aspects of internal analysis on your own company, along with method recommendations and further resources.</p>
        </div>

        <ul>
            <li><a class="reference internal" href="javascript:void(0);" onclick="showSubSection('organization structure')">Organization structure</a></li>
            <li><a class="reference internal" href="javascript:void(0);" onclick="showSubSection('company objective')">Company objective</a></li>
            <li><a class="reference internal" href="javascript:void(0);" onclick="showSubSection('core competencies')">Core competencies</a></li>
            <li><a class="reference internal" href="javascript:void(0);" onclick="showSubSection('customer base')">Customer base</a></li> 
            <li><a class="reference internal" href="javascript:void(0);" onclick="showSubSection('marketing & branding')">Marketing & Branding</a></li>  
            <li><a class="reference internal" href="javascript:void(0);" onclick="showSubSection('research & development')">Research & Development</a></li>  
            <li><a class="reference internal" href="javascript:void(0);" onclick="showSubSection('customer relationship management')">Customer relationship management</a></li>  
            <li><a class="reference internal" href="javascript:void(0);" onclick="showSubSection('technology infrastructure')">Technology infrastructure</a></li>                            
        </ul>
        <div class="subsection" id="organization structure" style="display: none;">
    <h3>Organization structure</h3>
    <div class="subsection-content">
        <p class="subsection-description">Organizational structure outlines how tasks are divided, coordinated, and controlled to achieve the company's goals and objectives efficiently. It defines:</p>
        <ul class="subsection-list">
            <li>Reporting lines</li>
            <li>Decision-making processes</li>
            <li>Communication channels</li>
            <li>The overall framework for how work is managed and executed</li>
        </ul>
    </div>
</div>
<div class="subsection" id="company objective" style="display: none;">
    <h3>Company objective</h3>
    <div class="subsection-content">
        <p class="subsection-description">Company objectives are specific, measurable, and time-bound goals that an organization sets to guide its actions and measure its success. Company objectives can encompass various aspects of the business, including:</p>
        <ul class="subsection-list">
            <li>Financial performance</li>
            <li>Market share</li>
            <li>Customer satisfaction</li>
            <li>Innovation</li>
            <li>Employee development</li>
            <li>Sustainability goals</li>
        </ul>
    </div>
</div>
<div class="subsection" id="core competencies" style="display: none;">
    <h3>Core competencies</h3>
    <div class="subsection-content">
        <p class="subsection-description">
            <strong>Definition:</strong> Core competencies are a company’s unique strengths, capabilities, and resources that set it apart from competitors and enable it to create value and achieve a competitive advantage in the marketplace.
        </p>
        <p class="subsection-description">
            <strong>Importance:</strong> These competencies are central to the company's ability to deliver its products or services effectively, meet customer needs, and drive sustainable growth.
        </p>
        <p class="subsection-description">
            <strong>Function:</strong> Core competencies serve as the foundation for a company's strategic direction and often define its identity and value proposition.
        </p>
    </div>
</div>
<div class="subsection" id="customer base" style="display: none;">
    <h3>Customer base</h3>
    <div class="subsection-content">
        <p class="subsection-description">
            A company's customer base refers to the group of individuals, organizations, or entities that regularly purchase or use the company's products or services. It is the core audience that the company targets and serves. The customer base is a critical aspect of a company's business strategy and a key influence on the company's revenue, market share, and overall success.
        </p>
    </div>
</div>
<div class="subsection" id="marketing & branding" style="display: none;">
    <h3>Marketing & Branding</h3>
    <div class="subsection-content">
        <p class="subsection-description">
            A company's marketing and brand strategy is a comprehensive plan that outlines how the company will promote its products or services, establish a strong brand identity, and achieve its business objectives in the market.
        </p>
    </div>
</div>

<div class="subsection" id="research & development" style="display: none;">
    <h3>Research & Development</h3>
    <div class="subsection-content">
        <p class="subsection-description">
            A company's Research & Development (R&D) strategy outlines its approach to innovation, technological advancement, the creation of new products, services, or processes, improving existing offerings, exploring new opportunities, and staying ahead of competitors in a rapidly evolving market.
        </p>
    </div>
</div>

<div class="subsection" id="customer relationship management" style="display: none;">
    <h3>Customer relationship management</h3>
    <div class="subsection-content">
        <p class="subsection-description">
            <strong>Definition:</strong> CRM strategy outlines how the organization plans to build, manage, and enhance its relationships with customers throughout their lifecycle.
        </p>
        <p class="subsection-description">
            <strong>The Goal:</strong> CRM strategy aims to create positive interactions, deliver exceptional customer experiences, and foster long-term loyalty.
        </p>
        <p class="subsection-description">
            <strong>The Content:</strong> CRM strategy involves various practices, technologies, and processes that enable the company to understand, engage, and serve its customers effectively.
        </p>
    </div>
</div>
<div class="subsection" id="technology infrastructure" style="display: none;">
    <h3>Technology infrastructure</h3>
    <div class="subsection-content">
        <p class="subsection-description">
            <strong>Definition:</strong> A company's technology infrastructure refers to the underlying foundation of hardware, software, networks, and other technological components that enable the organization's IT operations, systems, and digital capabilities.
        </p>
        <p class="subsection-description">
            <strong>Goal:</strong> It should provide the necessary framework for information flow, communication, data storage, processing, and access across various departments and functions within the company.
        </p>
    </div>
</div>


    
    </div>

    <div class="section" id="external-analysis">
        <h2>External Analysis</h2>
        <p>An external analysis examines the external factors and forces that impact your organisation’s operating environment.
            They are forces and dynamics beyond your control, but still, impact your organisation level and position in the marketplaces
            </p>

        <ul>
            <li><a class="reference internal" href="javascript:void(0);" onclick="showSubSection('market segmentation')">Market segmentation</a></li>
            <li><a class="reference internal" href="javascript:void(0);" onclick="showSubSection('industry associations')">Industry associations</a></li>
            <li><a class="reference internal" href="javascript:void(0);" onclick="showSubSection('supplier relationships')">Supplier relationships</a></li> 
            <li><a class="reference internal" href="javascript:void(0);" onclick="showSubSection('competitor analysis')">Competitor analysis</a></li>  
            <li><a class="reference internal" href="javascript:void(0);" onclick="showSubSection('customer analysis')">Customer analysis</a></li>  
            <li><a class="reference internal" href="javascript:void(0);" onclick="showSubSection('environmental factors')">Environmental factors</a></li>  
        </ul>
        <div class="subsection" id="market segmentation" style="display: none;">
            <h3>Market segmentation</h3>
            <div class="subsection-content">
                <p>A market segmentation strategy is the process through which you identify, organise, research, and target a specific segment of a broad target market.
                    We can pull out a four step process for developing a segmentation strategy.
                    </p>
                    <p class="subsection-description">
                        <img src="Picture5.jpg" alt="ms" style="max-width: 60%;height:auto;">
                    </p>
            </div>
        </div>
        <div class="subsection" id="industry associations" style="display: none;">
            <h3>Industry associations</h3>
            <div class="subsection-content">
                <p>A market segmentation strategy is the process through which you identify, organise, research, and target a specific segment of a broad target market. We can pull out a four step process for developing a segmentation strategy.</p>
                <p>An industry association related to a market research guide would likely be an organization that represents and serves professionals, businesses, and stakeholders within the broader field of market research.</p>
                <p>Key functions of Industry Association are:</p>
                <ol class="subsection-description">
                    <li><strong>Networking Opportunities:</strong> Industry associations provide a platform for professionals to connect, share insights, and build relationships with others in the field. This networking can lead to collaboration and business opportunities.</li>
                    <li><strong>Collaboration and Partnerships:</strong> Associations foster collaboration among members, enabling them to work together on projects, research initiatives, and industry-wide efforts that benefit the entire market research community.</li>
                    <li><strong>Advancement of Innovation:</strong> Industry associations often play a role in advancing innovation by providing resources, education, and a space for members to exchange ideas and stay up-to-date with the latest trends and technologies.</li>
                </ol>
            </div>
        </div>
        <div class="subsection" id="supplier relationships" style="display: none;">
            <h3>Supplier relationships</h3>
            <div class="subsection-content">
                <p>Establishing strong supplier relationships is crucial when creating a market research guide. Suppliers play a significant role in providing the necessary resources, tools, and expertise to ensure the guide's accuracy, relevance, and effectiveness.</p>
                <p>Here are some key considerations:</p>
                <ol class="subsection-description">
                    <li><strong>Choose suppliers that align with the goals and quality standards.</strong> Select suppliers whose products or services align with the objectives of your market research guide and maintain high quality standards.</li>
                    <li><strong>Maintain open and transparent communication with your suppliers.</strong> Regularly communicate your requirements, expectations, and any changes to ensure a smooth collaboration.</li>
                    <li><strong>Implement quality control measures to ensure the guide's standards of accuracy.</strong> Put in place processes to review and verify the information provided by suppliers, ensuring it meets the required standards.</li>
                    <li><strong>Work with suppliers who are flexible and responsive to changes.</strong> Choose suppliers who can adapt to changes in the guide's content, scope, or timeline and provide timely updates.</li>
                    <li><strong>Develop contingency plans to mitigate risks.</strong> Anticipate potential challenges or disruptions in the supplier relationship and have backup plans in place to minimize their impact.</li>
                    <li><strong>Consider building long-term partnerships with reliable and reputable suppliers.</strong> Establishing strong and lasting relationships can lead to more effective collaborations and consistent guide quality over time.</li>
                </ol>
            </div>
        </div>
        <div class="subsection" id="competitor analysis" style="display: none;">
            <h3>Competitor analysis</h3>
            <div class="subsection-content">
                <p>Your competitor analysis will look at three different types of competitors:</p>
                <ul class="subsection-description">
                    <li><strong>Direct competitors:</strong> These are businesses operating in your direct market space. They are often listed alongside you in customer shortlists. Analyze their offerings, strengths, weaknesses, and market positioning.</li>
                    <li><strong>Indirect competitors:</strong> These competitors aren't in your exact market sphere but can still impact your business. Keep an eye on them because they might evolve into direct competitors. Monitor their activities and potential threats.</li>
                    <li><strong>Substitutes or new entrants:</strong> These are entities with alternative products or services. While they might not be direct competition now, they could disrupt your market in the future. Monitor their growth and assess their potential impact.</li>
                </ul>
                <p class="subsection-description">
                    <img src="Picture6.jpg" alt="ms" style="max-width: 60%;height:auto;">
                </p>
            </div>
        </div>
        <div class="subsection" id="customer analysis" style="display: none;">
            <h3>Customer analysis</h3>
            <div class="subsection-content">
                <ul class="subsection-description">
                    <li><strong>Customer analysis for a market research guide involves understanding the needs, preferences, behaviors, and challenges of the guide's intended audience.</strong> This insight is essential for tailoring the guide's content, format, and delivery to effectively meet the expectations of your target customers.</li>
                    <li><strong>Segment your target audience based on common characteristics, needs, and preferences.</strong> Divide your audience into groups that share similar traits, allowing you to customize your guide for each segment.</li>
                    <li><strong>Analyze how your audience interacts with similar resources.</strong> Understand how your audience currently engages with other guides or resources in the market research field.</li>
                    <li><strong>Determine how your audience prefers to consume information.</strong> Identify whether your audience prefers written content, visual aids, videos, or interactive formats.</li>
                    <li><strong>Include case studies, examples, and practical scenarios that resonate with your audience's professional experiences.</strong> Real-world examples make the content relatable and applicable.</li>
                    <li><strong>Develop detailed buyer personas that represent different segments of your target audience.</strong> Personas help you visualize your audience, their needs, and their behaviors.</li>
                    <li><strong>Once the guide is available, actively seek feedback from your audience.</strong> Continuous feedback allows you to refine and improve the guide based on real-world use and responses.</li>
                </ul>
            </div>
        </div>
        <div class="subsection" id="environmental factors" style="display: none;">
            <h3>Environmental factors</h3>
            <div class="subsection-content">
                <p>Environmental factors in the context of a market research guide refer to the external influences and conditions that can impact the creation, distribution, and effectiveness of the guide.</p>
                <p>Some key environmental factors to consider:</p>
                <ol class="subsection-description">
                    <li><strong>Technological Advancements:</strong> Stay updated on technological developments that may affect how your guide is created, distributed, and accessed.</li>
                    <li><strong>Digital Transformations:</strong> The shift to digital platforms can change how audiences engage with content, affecting the guide's format and delivery methods.</li>
                    <li><strong>Economic Conditions:</strong> Economic fluctuations can impact the demand for your guide and influence the resources available for its creation.</li>
                    <li><strong>Globalization and Localization:</strong> Consider the global reach of your guide and how it might need to be tailored for different regions or languages.</li>
                    <li><strong>Competition and Market Trends:</strong> Analyze the competitive landscape and current market trends to ensure your guide remains relevant and unique.</li>
                    <li><strong>Education:</strong> Changes in educational methods or requirements may influence how your guide is structured and presented.</li>
                    <li><strong>Public Trust:</strong> Consider how public perception and trust in information sources may impact the credibility of your guide.</li>
                    <li><strong>Online Communities:</strong> Engage with online communities to understand discussions and concerns related to your guide's topic.</li>
                    <li><strong>Cultural Shifts:</strong> Cultural changes can affect how your guide's content is perceived and received by diverse audiences.</li>
                    <li><strong>Industry Disruption:</strong> Be aware of potential disruptions in your industry that could affect the relevance or viability of your guide.</li>
                </ol>
            </div>
        </div>
        
        
              




    </div>


    <div class="section" id="ethical-considerations">
    <h2>Ethical Considerations</h2>
    <div class="subsection-content">
        <p class="subsection-description">
            Ethical considerations are crucial in market research to ensure that the rights and well-being of participants, clients, researchers, and the broader society are respected and protected. Adhering to ethical principles enhances the credibility and reliability of research outcomes. Here are key ethical considerations to keep in mind when conducting market research:
        </p>
        <ul class="subsection-list">
            <li><strong>Informed Consent</strong>: Participants should provide voluntary and informed consent to participate in the research. They should be fully aware of the purpose, procedures, risks, benefits, and any potential uses of their data.</li>
            <li><strong>Privacy and Confidentiality</strong>:
                <ul>
                    <li>Protect participants' privacy by anonymizing and aggregating data whenever possible.</li>
                    <li>Safeguard participants' confidential information, ensuring that it is stored securely and not shared with unauthorized parties.</li>
                    <li>Clearly communicate how participant data will be used, who will have access to it, and how long it will be retained.</li>
                </ul>
            </li>
            <li><strong>Data Collection and Use</strong>:
                <ul>
                    <li>Collect only the data necessary for the research and use it solely for the intended purpose. </li>
                    <li>Be transparent about data collection methods, ensuring they are appropriate and respectful of participants' rights. </li>
                    <li>Minimize any potential harm to participants through data collection or analysis.</li>
                </ul>
                <li><strong>Avoid Deception</strong>:
                <ul>
                    <li>Do not deceive or mislead participants about the purpose or nature of the research.</li>
                    <li> If deception is necessary for the study, thoroughly debrief participants afterward, explaining the true nature of the research and addressing any concerns.</li>
                </ul>
                <li><strong>Conflicts of Interest</strong>:
                <ul>
                    <li>Disclose any potential conflicts of interest that could influence the research process or outcomes.</li>
                    <li>Maintain objectivity and avoid bias in the design, execution, and reporting of the research.</li>
                </ul>
                <li><strong>Respect for Diversity and Inclusion</strong>:
                <ul>
                    <li>Ensure that research samples are representative and diverse, reflecting the target population.</li>
                    <li>Treat all participants with respect, regardless of their demographic characteristics or opinions.</li>
                </ul>
                <li><strong>Honesty and Transparency</strong>:
                <ul>
                    <li>Provide accurate and truthful information about the research objectives, methods, and potential implications.</li>
                    <li>Clearly communicate the limitations of the research and any uncertainties in the findings.</li>
                </ul>
                <li><strong>Minimize Harm</strong>:
                <ul>
                    <li>Take measures to prevent physical, emotional, or psychological harm to participants, researchers, or any stakeholders.</li>
                    <li>Consider the potential impact of the research on vulnerable or sensitive populations.</li>
                </ul>
                <li><strong>Responsible Reporting</strong>:
                <ul>
                    <li>Present research findings accurately, avoiding selective or biased reporting.</li>
                    <li>Clearly distinguish between opinion, interpretation, and factual data.</li>
                </ul>
                <li><strong>Compliance with Laws and Regulations</strong>:
                <ul>
                    <li>Adhere to relevant laws, regulations, and industry standards related to data protection, privacy, and research ethics.</li>
                    <li>Obtain necessary approvals from institutional review boards (IRBs) or ethics committees if required.</li>   
                </ul>
                <li><strong>Accountability</strong>:
                <ul>
                    <li>Take responsibility for the ethical conduct of the research and address any ethical concerns that arise during the process.</li>
                    <li>Be open to feedback and address any ethical concerns raised by participants, colleagues, or stakeholders.</li>
                <p>By considering and addressing these ethical considerations, market researchers can ensure that their work is conducted in a responsible, respectful, and morally sound manner.</p>
                    </ul>

        </ul>
    </div>
</div>

    
    <div class="section" id="findings" style="display: none;">
        <h3>Present your findings</h3>
        <div class="subsection-content">
            <p>After necessary research, data collection and analysis, presenting your market research findings effectively is equally crucial to ensure that your audience understands and engages with the information you've gathered. Here are some methods and forms of presentation you can consider:</p>
            
            <p><strong>Methods</strong></p>
            <ul>
                <li><strong>In-Person Presentation:</strong> This is a traditional method where you deliver your findings to your audience face-to-face. It allows for real-time interaction and clarification of doubts.</li>
                <li><strong>Virtual Presentation:</strong> With the rise of remote work and online meetings, presenting findings through video conferencing platforms is becoming increasingly common. This method can be particularly useful for reaching a global audience.</li>
                <li><strong>Written Reports:</strong> Prepare a comprehensive report that includes all the details of your market research. This can be shared digitally or in print.</li>
                <li><strong>Infographics and Visuals:</strong> Create visually appealing infographics, charts, and graphs to convey complex data in a more digestible manner.</li>
                <li><strong>Webinars and Workshops:</strong> Conduct online webinars or workshops to present your research. This allows for a mix of visual aids, live explanations, and Q&A sessions.</li>
            </ul>
            
            <p><strong>Formats</strong></p>
            <ul>
                <li><strong>Executive Summary:</strong> Begin with a concise summary of the most important findings, conclusions, and recommendations. This is particularly useful for busy executives who need a quick overview.</li>
                <li><strong>Slide Presentation:</strong> Use PowerPoint or other presentation software to create slides that outline your research process, data, analysis, and conclusions.</li>
                <li><strong>Interactive Dashboards:</strong> Develop interactive dashboards using tools like Tableau or Power BI. This allows users to explore the data themselves and draw their own insights.</li>
                <li><strong>Case Studies:</strong> Present real-world scenarios that illustrate how your market research findings can be applied to solve specific problems or capture opportunities.</li>
                <li><strong>Comparative Analysis:</strong> Compare your findings with previous research or industry benchmarks to provide context and insights.</li>
            </ul>
        </div>
    </div>
    

    <div class="section" id="recommendations" style="display: none;">
        <h3>Recommendations</h3>
        <div class="subsection-content">
            <p>These recommended data sources are collected through survey, interview, workshops, and our secondary data research.</p>
            <p><strong>Secondary data sources:</strong></p>
            <div style="overflow-x:auto;">
                <table class="data-table">
                    <tr>
                        <th>Data source</th>
                        <th>Example</th>
                        <th>Key search terms</th>
                    </tr>
                    <tr>
                        <td>Universities/research organizations</td>
                        <td>Local Universities, local research centers (e.g., University of Bremen)</td>
                        <td>Location; university/research center</td>
                    </tr>
                    <tr>
                        <td>Industry association</td>
                        <td>E.g., Autonomous Vehicle Industry Association (<a href="https://theavindustry.org/">https://theavindustry.org/</a>)</td>
                        <td>Product name; business area; industry association</td>
                    </tr>
                    <tr>
                        <td>Government release</td>
                        <td>Financial report directory (e.g., Germany <a href="https://www.unternehmensregister.de/ureg/howto1.9.html?submitaction=language&language=en">https://www.unternehmensregister.de/ureg/howto1.9.html?submitaction=language&language=en</a>); Patent directory (e.g., Germany <a href="https://www.dpma.de/english/index.html">https://www.dpma.de/english/index.html</a>)</td>
                        <td>Location, official, financial report, patent, etc.</td>
                    </tr>
                    <tr>
                        <td>News paper/magazines/publications/books</td>
                        <td>Harvard Business Review; Financial Time, etc.</td>
                        <td>Product name; business area; news; book; research; name of the magazine</td>
                    </tr>
                    <tr>
                        <td>Databases</td>
                        <td>Local library databases (e.g., University Bremen purchased databases <a href="https://elib.suub.uni-bremen.de/cgi-bin/CiXbase/internet/CiXbase_search?act=search&term=wiw&index=C&ORDER=IA&dtyp=b&section=f&XML_STYLE=/CiXbase/internet/styles/list-ger.xml&project=internet&rtyp=d">https://elib.suub.uni-bremen.de/cgi-bin/CiXbase/internet/CiXbase_search?act=search&term=wiw&index=C&ORDER=IA&dtyp=b&section=f&XML_STYLE=/CiXbase/internet/styles/list-ger.xml&project=internet&rtyp=d</a>)</td>
                        <td>Name of local Universities, business area, product name, database</td>
                    </tr>
                    <tr>
                        <td>Conference (Business, Academic)</td>
                        <td>Autonomous Vehicle Conference (<a href="https://www.europe.autonomous-vehicles-conference.com/">https://www.europe.autonomous-vehicles-conference.com/</a>)</td>
                        <td>Product name; business area; conference</td>
                    </tr>
                    <tr>
                        <td>Business press release</td>
                        <td>Local business release collection (e.g., Germany: <a href="https://www.presseportal.de/">https://www.presseportal.de/</a>), company website (e.g., TOPAS <a href="https://topas.tech/aktuelles/topas-in-der-presse/">https://topas.tech/aktuelles/topas-in-der-presse/</a>)</td>
                        <td>Product name; business area; business release / directly from company website</td>
                    </tr>
                    <tr>
                        <td>Consulting/research services</td>
                        <td>CB Insights (<a href="https://www.cbinsights.com/">https://www.cbinsights.com/</a>); TechCrunch (<a href="https://techcrunch.com/">https://techcrunch.com/</a>)</td>
                        <td>Product name; business area; consult service; research service</td>
                    </tr>
                    <tr>
                        <td>Search engines / AI chatbot</td>
                        <td>Google, chatGPT, consensus (<a href="https://consensus.app/search/">https://consensus.app/search/</a>)</td>
                        <td>/</td>
                    </tr>
                </table>
                <p><strong>Databases:</strong></p>
                <ul>
                    <li><a href="https://www.dowjones.com/professional/">Dow Jones</a></li>
                    <li><a href="https://www.dowjones.com/professional/factiva/">Factiva</a></li>
                    <li><a href="https://www.orbis.de/en/">Orbis</a></li>
                    <li><a href="https://www.ebsco.com/">Ebsco</a></li>
                    <li><a href="https://www.ieee.org/">IEEE</a></li>
                    <li><a href="https://www.wiso-net.de/login?targetUrl=%2Fdosearch">Wiso.net</a></li>
                    <li><a href="https://www.ft.com/ft-data">Financial Times Data</a></li>
                    <li><a href="https://www.jstor.org/">J Stor</a></li>
                    <li><a href="https://www.statista.com/">Statista</a></li>
                </ul>
                <p><strong>Books:</strong></p>
        <ul>
            <li><a href="https://www.amazon.de/-/en/Donna-Tedesco/dp/0124047009">The Moderator's Survival Guide</a> by Donna Tedesco and Fiona Tranquada.</li>
            <li><a href="https://methods.sagepub.com/">SAGE Research Methods</a>: Offers articles, videos, and other resources on research methods, including qualitative interviews.</li>
            <li><a href="https://us.sagepub.com/en-us/nam/handbook-of-marketing-scales/book234436">Handbook of Marketing Scales</a>: Learn to design your scale questions with various marketing scales.</li>
        </ul>
        <p><strong>Websites for market research methods:</strong></p>
        <ul>
            <li><a href="https://conjointly.com/kb/">Research Methods Knowledge Base</a>: Provides a comprehensive overview of various research methods.</li>
            <li><a href="https://www.greenbook.org/mr/focus-groups/">GreenBook Blog</a>: Offers a range of articles, webinars, and resources on market research methods.</li>
            <li><a href="https://www.qrca.org/">Qualitative Research Consultants Association (QRCA)</a>: Offers resources, webinars, and articles related to qualitative research methods.</li>
            <li><a href="https://www.hubspot.com/">Hubspot</a>: Offers business and marketing trainings, market research tools recommendation.</li>
        </ul>
        <p><strong>Analytical tools:</strong></p>
        <ul>
            <li><a href="https://docs.google.com/presentation/d/1TY_u23n5Lm3gNtrkvFKLUbZW-ybScpGwo9e2ZLRAmcA/copy">Five forces analysis</a> @ external analytical tools encompassing analyses for Competitive Rivalry, Threat of New Entrants, Threat of Substitution, Buyer Power, and Supplier Power, Template from Hubspot.</li>
            <li><a href="https://docs.google.com/document/d/1-_1pYcP3J3f6Z6eFRxAET_P-EvwkIZYs0rbckcXrfYI/copy">SWOT analysis</a> @ internal analytical tools encompassing analyses for Strengths, Weaknesses, Opportunities and Threats, Template from Hubspot.</li>
        </ul>
        <p><strong>Design tools for presenting results:</strong></p>
        <ul>
            <li><a href="https://www.canva.com/">Canva</a> @ slides, poster, brochure templates</li>
            <li><a href="https://unsplash.com/">Unsplash</a> @ sources for visuals</li>
        </ul>
        <p><strong>Learning resources:</strong></p>
        <ul>
            <li><a href="https://www.linkedin.com/learning/market-research-foundations/the-power-of-market-research?resume=false&u=38239804">LinkedIn Learning @ Market Research Foundation</a></li>
            <li><a href="https://www.coursera.org/learn/market-research">Coursera @ Market research and customer behaviours</a></li>
            <li>Or, search market research courses on these general learning platforms: LinkedIn Learning, Coursera, Udemy, Khan Academy, W3, etc.</li>
        </ul>
        <p><strong>From our survey:</strong></p>
        <p>Top sources: TBA</p>
            </div>
        </div>
    </div>
    

    <div class="section" id="conclusion" style="display: none;">
        <h3>Conclusion</h3>
        <div class="subsection-content">
            <p>We hope this guide has provided you with valuable insights, strategies, and tools to enhance your market research efforts.</p>
            <p>As you embark on your market research journey, remember these three key points:</p>
            
            <ol>
                <li><strong>Knowledge is Power:</strong> Understanding your target audience, industry trends, and competitive landscape empowers you to make informed decisions that drive business growth.</li>
                <li><strong>Evolving Strategies:</strong> Continuously adapt your strategies to align with changing consumer behaviors, emerging technologies, and evolving market conditions.</li>
                <li><strong>Data-driven Insights:</strong> Utilize data-driven insights to refine your marketing campaigns, product development, and business strategies.</li>
            </ol>
        </div>
    </div>
    
    <div class="section" id="references" style="display: none;">
        <h3>References</h3>
        <div class="subsection-content">
            <p>For further reading and resources, you can refer to the following:</p>
            
            <ul>
                <li><a href="https://en.wikipedia.org/wiki/Market_research">Wikipedia - Market Research</a></li>
                <li><a href="https://topas.tech/referenzen/referenz/echte-robotik/">TOPAS - Case Study: Echte Robotik</a></li>
                <li><a href="https://www.hubspot.com/">HubSpot</a></li>
                <li><a href="https://onstrategyhq.com/resources/internal-and-external-analysis/">OnStrategy - Internal and External Analysis</a></li>
            </ul>
        </div>
    </div>
    

    <div class="section" id="feedback" style="display: none;">
        <h3>Feedback</h3>
        <div class="subsection-content">
            <p>Thank you for choosing our market research guide as your resource for insights and strategies. We are dedicated to continuously improving and enhancing the guide to better serve your needs. If you have any suggestions, thoughts, and feedback, please use the following link to tell us what you think. Your feedback is invaluable in helping us achieve this goal.</p>
            <p><a href="https://docs.google.com/forms/d/e/1FAIpQLSfrSBi2DY38fT0dTtVYejOToE_z9iti9PASNXLZDeuef0_WkQ/viewform?usp=sf_link">Google Form link for feedback</a></p>
        </div>
    </div>
    
</div>
</div>
</body>
</html>
