var quotes = [100];

var quotes = [
    "<p>It\'s only after you\'ve stepped outside your comfort zone that you begin to change, grow, and transform. \-Roy T. Bennett</p>",
    "<p>Do what is right, not what is easy nor what is popular. \-Roy T. Bennett, The Light in the Heart</p>",
    "<p>Believe in yourself. You are braver than you think, more talented than you know, and capable of more than you imagine. \-Roy T. Bennett, The Light in the Heart</p>",
    "<p>Be yourself; everyone else is already taken.\― Oscar Wilde</p>",
    "<p>Be the change that you wish to see in the world.\― Mahatma Gandhi</p>",
    "<p>Live as if you were to die tomorrow. Learn as if you were to live forever.\― Mahatma Gandhi</p>"
  ]
  
  
  function newQuote() {
    var randomNumber = Math.floor(Math.random() * (quotes.length));
    document.getElementById('quoteDisplay').innerHTML = quotes[randomNumber];
  }
  
  function saveQuote() {
     var getInput = document.getElementById('quoteDisplay').innerHTML;
     localStorage.setItem("setQuote",getInput);
     localStorage.setItem("setQuoteForm",getInput);
  }

  function saveQuoteForm() {
    var getInput = document.getElementById('quote').value;
    getInput = "<p>" + getInput + "</p>";
    localStorage.setItem("setQuoteForm",getInput);
    localStorage.setItem("setQuote",getInput);
 }

  function addQuotes() {
    var boxvalue = document.getElementById('quote').innerHTML;
    
    if (boxvalue == null)
    {
        
            document.getElementById('quoteDisplay').innerHTML =  "<p>Click the button for a quote.</p>";
    }
    else
    {
      quotes.push(boxvalue);
      console.log(quotes);
            document.getElementById('quoteDisplay').innerHTML = "<p>" + boxvalue + "</p>";
    }
  
  }
  
  function useQuote() {
       var quote = localStorage.getItem("setQuote");
       var quoteForm = localStorage.getItem("setQuoteForm");
  if (quote == null)
  {
      quote = "<p>Click the button for a quote.</p>"
          document.getElementById('quoteDisplay').innerHTML = quote;
  }
  else
  {
          document.getElementById('quoteDisplay').innerHTML = quote;
  }
  }

  function openForm() {
    if(document.getElementById("CustomQuote").style.display == "block")
    {
      document.getElementById("CustomQuote").style.display = "none";
    }
    else{
      document.getElementById("CustomQuote").style.display = "block";
    }
  }

  function openFormB() {
    if(document.getElementById("settingsHome").style.display == "block")
    {
      document.getElementById("settingsHome").style.display = "none";
    }
    else{
      document.getElementById("settingsHome").style.display = "block";
    }
  }
  
  function closeForm() {
    document.getElementById("CustomQuote").style.display = "none";
  }

  function closeFormB() {
    document.getElementById("settingsHome").style.display = "none";
  }