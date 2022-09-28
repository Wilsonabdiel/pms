document.addEventListener('DOMContentLoaded', function() {

    // Use buttons to toggle between views
    document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
    document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
    document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
    document.querySelector('#compose').addEventListener('click', compose_email);
    document.querySelector('#compose-form').addEventListener('submit', send_email);
  
    // By default, load the inbox
    load_mailbox('inbox');
  });
  function send_email(){
    event.preventDefault();
    // Store info from user
    const recipient = document.querySelector('#compose-recipients').value;
    const subject = document.querySelector('#compose-subject').value;
    const body = document.querySelector('#compose-body').value;
    // Send Email to my backend
    fetch('/emails', {
      method: 'POST',
      body: JSON.stringify({
          recipients: recipient,
          subject: subject,
          body: body
      })
    })
    .then(response => response.json())
    .then(result => {
        // Print result
        console.log(result);
        load_mailbox('sent');
    });
  
  }
  function compose_email() {
  
    // Show compose view and hide other views
    document.querySelector('#emails-view').style.display = 'none';
    document.querySelector('#compose-view').style.display = 'block';
    document.querySelector('#emails-view-detail').style.display = 'none';
  
    // Clear out composition fields
    document.querySelector('#compose-recipients').value = '';
    document.querySelector('#compose-subject').value = '';
    document.querySelector('#compose-body').value = '';
  }
  function viewEmail(id) {
    fetch(`/emails/${id}`)
      .then(response => response.json())
      .then(email => {
          // Print email
          console.log(email);
          document.querySelector('#emails-view').style.display = 'none';
          document.querySelector('#compose-view').style.display = 'none';
          document.querySelector('#emails-view-detail').style.display = 'block';
  
          document.querySelector('#emails-view-detail').innerHTML= `
          <ul class="list-group">
          <li class="list-group-item active"><strong>From: </strong>${email.sender}</li>
          <li class="list-group-item active"><strong>To: </strong>${email.recipients}</li>
          <li class="list-group-item active"><strong>Subject: </strong>${email.subject}</li>
          <li class="list-group-item active"><strong>Timestamp: </strong>${email.timestamp}</li>
          <li class="list-group-item active"><strong>${email.body}</li>
          
          
         
        </ul>
          `;
          
        const btnreply = document.createElement('button');
        btnreply.innerHTML = 'Reply';
        btnreply.className = "btn btn-light";
        btnreply.addEventListener('click', function() {
  
          compose_email();
        document.querySelector('#compose-recipients').value = email.sender;
        let subject = email.subject;
        if (subject.split(' ',1[0] != "Re:")){
          subject = "Re: "+ email.subject;
        }
        document.querySelector('#compose-subject').value = subject ;
        document.querySelector('#compose-body').value = `On ${email.timestamp} ${email.sender} wrote: `;
      
  
        });
        document.querySelector('#emails-view-detail').append(btnreply); 
        
  
            
          
        
        
  
          // ... archive ND unarchive...
  
          const btnarc = document.createElement('button');
          btnarc.innerHTML = email.archived ? "Unarchive": "Archive";
          btnarc.className = email.archived ? "btn btn-success ":"btn btn-danger ";
          btnarc.addEventListener('click', function() {
            fetch(`/emails/${email.id}`, {
              method: 'PUT',
              body: JSON.stringify({
                  archived: !email.archived
              })
            })
            .then(() => { load_mailbox('archive')})
          });
          document.querySelector('#emails-view-detail').append(btnarc);
              });
      
  }
  function load_mailbox(mailbox) {
    
    // Show the mailbox and hide other views
    document.querySelector('#emails-view').style.display = 'block';
    document.querySelector('#compose-view').style.display = 'none';
    document.querySelector('#emails-view-detail').style.display = 'none';
    // Show the mailbox name
    document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;
  
    fetch(`/emails/${mailbox}`)
      .then(response => response.json())
      .then(emails => {
          // Print emails
          
          // Loop through emails
          emails.forEach(eachEmail => {
  
            console.log(eachEmail);
            const newEmail = document.createElement('div');
            newEmail.className = "list list-group-item"
            newEmail.innerHTML = `
            <h6>Sender: ${eachEmail.sender}</h6>
            <h5>Subject: ${eachEmail.subject}</h5>
            <p>${eachEmail.timestamp}</p>
            `;
            newEmail.className = eachEmail.read ? 'read':'unread';
            newEmail.addEventListener('click',function(){ viewEmail(eachEmail.id)});
            document.querySelector('#emails-view').append(newEmail);
                  });
                  
          // ... do something else with emails ...
      });
  
  }
  