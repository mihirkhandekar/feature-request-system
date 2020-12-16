import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from "@angular/forms";
import { HttpClient } from '@angular/common/http';


@Component({
  selector: 'app-view-feedback',
  templateUrl: './view-feedback.component.html',
  styleUrls: ['./view-feedback.component.css']
})

/*export class Parameters {
  'date': string;
  'name': string;
  'description': string;
  'client': string;
}*/

export class ViewFeedbackComponent implements OnInit {

  headers = ["ID", "Name", "Age", "Gender", "Country"];
  responseArray: any

  constructor(
    private http: HttpClient
  ) {
    this.http.get('http://localhost:5000/api/featurerequest').subscribe(
      (response) => {
        console.log(response)
        this.responseArray = response
      }
    )

  }

  ngOnInit() {
  }


}
