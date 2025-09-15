typing_indicator_animation = """
    <style>
    .typing-indicator {
    display: inline-flex;
    align-items: center;
    background: transparent;
    border-radius: 15px;
    padding: 6px 12px;
    margin: 5px 0;
    }
    .typing-dots span {
    width: 6px;
    height: 6px;
    margin: 0 2px;
    background-color: #ffffff;
    border-radius: 50%;
    display: inline-block;
    animation: bounce 1.4s infinite;
    }
    .typing-dots span:nth-child(2) { animation-delay: 0.2s; }
    .typing-dots span:nth-child(3) { animation-delay: 0.4s; }
    @keyframes bounce {
    0%, 80%, 100% { transform: scale(0); }
    40% { transform: scale(1); }
    }
    </style>
"""

typing_indicator = """
                        <div class='typing-indicator'><div class='typing-dots'>
                        <span></span><span></span><span></span>
                        </div></div>
                    """

headr = "<h1 class=hdr>Neutron</h1>"

instructions = """
                <div style="font-size: 12px; line-height: 1.5;">
                    ❓ How to use:<br>
                    <ul>
                        <li>Chat with Neutron as you like.</li>
                        <li>To attach a link of a website just give it in the chatbox.</li>
                        <li>To upload a file (.txt or .pdf) use the side panel.</li>
                        <li>If you want to get an answer from the uploaded files or provided links, use the prompt:
                        <b>File: &ltyour query&gt</b> or <b>Web: &ltyour query&gt</b>.</li>
                    </ul>
                </div>
            """

extracss = """
        <style>
            .hdr{
                text-shadow: 0px 0px 15px red;
                animation: colranim 15s ease infinite;
            }
            @keyframes colranim {
            0%{
                text-shadow: 0px 0px 15px red;
            }
            10%{
                text-shadow: 0px 0px 15px cyan;
            }
            20%{
                text-shadow: 0px 0px 15px green;
            }
            30%{
                text-shadow: 0px 0px 15px blue;
            }
            40%{
                text-shadow: 0px 0px 15px yellow;
            }
            50%{
                text-shadow: 0px 0px 15px magenta;
            }
            60%{
                text-shadow: 0px 0px 15px hotpink;
            }
            70%{
                text-shadow: 0px 0px 15px orange;
            }
            80%{
                text-shadow: 0px 0px 15px smokewhite;
            }
            90%{
                text-shadow: 0px 0px 15px purple;
            }
            100%{
                text-shadow: 0px 0px 15px red;
            }
        }
            /* Hide Streamlit's main menu (hamburger menu) */
            header {visibility: hidden;}

            /* Hide Streamlit's footer */
            footer {visibility: hidden;}

            /* Hide the watermark ("Made with Streamlit") */
            .st-emotion-cache-z5fcl4 {display: none;}
        </style>
    """

footer = """
            <div style="
            position: fixed; 
            bottom: 0; 
            left: 0; 
            width: 100%; 
            background-color: rgba(0,0,0,0.5); 
            color: white; 
            text-align: center; 
            padding: 10px; 
            font-size: 14px;
        ">
            👨‍💻 Developed by <a style='color:red; text-decoration:none;' href='https://arnabsingha200228.github.io/'>Arnab Singha</a><br>
        </div>
    """
