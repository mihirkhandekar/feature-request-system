import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from "@angular/forms";
import { HttpClient } from '@angular/common/http';


@Component({
  selector: 'app-submit-feedback',
  templateUrl: './submit-feedback.component.html',
  styleUrls: ['./submit-feedback.component.css']
})

export class SubmitFeedbackComponent implements OnInit {
  form: FormGroup;
  respMessage: string = '';
  errorMessage:string = '';
  warningMessage:string = '';
  today=new Date()
  constructor(
    public fb: FormBuilder,
    private http: HttpClient
  ) {
    this.form = this.fb.group({
      name: [''],
      description: [''],
      client: [''],
      date: [''],
      priority: [''],
      productarea: ['']
    })
  }

  ngOnInit() { 
    this.respMessage = ''
    this.errorMessage = ''
    this.warningMessage = ''
  }


  submitForm() {
    this.respMessage = ''
    this.errorMessage = ''
    this.warningMessage = ''

    var formData: any = new FormData();
    formData.append("name", this.form.get('name').value);
    formData.append("description", this.form.get('description').value);
    formData.append("client", this.form.get('client').value);
    formData.append("date", this.form.get('date').value);
    formData.append("priority", this.form.get('priority').value);
    formData.append("productarea", this.form.get('productarea').value);

    this.http.post('http://localhost:5000/api/featurerequest', formData).subscribe(
      (response:Response) => {
        console.log(response);
        var message = response['message']
        var sim = response['similarity_count']
        if(sim > 0) {
          console.log('Multiple case')
          this.warningMessage = 'There already exist ' + sim + ' similar feature requests!'
        }
        this.respMessage = message;
        
      },
      (error) => {
        console.log(error);
        this.errorMessage = 'Error in adding. Please check your input.  '
      }
    )
  }

}
