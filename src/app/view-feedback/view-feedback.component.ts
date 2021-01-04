import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from "@angular/forms";
import { HttpClient } from '@angular/common/http';
import {MatPaginatorModule} from '@angular/material/paginator';


@Component({
  selector: 'app-view-feedback',
  templateUrl: './view-feedback.component.html',
  styleUrls: ['./view-feedback.component.css']
})


export class ViewFeedbackComponent implements OnInit {

  headers = ["ID", "Name", "Age", "Gender", "Country"];
  responseArray: any;
  length: any;
  pageIndex: any;
  pageSize: any;

  constructor(
    private http: HttpClient
  ) {
    var ip = window.location.hostname
    this.http.get('http://'+ip+':5000/api/featurerequest?page=1').subscribe(
      (response) => {
        this.responseArray = response['data']
        this.length = response['pagination']['totalElements']
        this.pageIndex = 0
        this.pageSize = 8

      }
    )
  }

  getServerData(event){
    var newPageIndex = event['pageIndex'] + 1
    var ip = window.location.hostname
    this.http.get('http://'+ip+':5000/api/featurerequest?page=' + newPageIndex).subscribe(
      (response) => {
        this.pageIndex = newPageIndex - 1
        this.pageSize = 8
        this.responseArray = response['data']
        this.length = response['pagination']['totalElements']
      }
    )
  }

  ngOnInit() {
  }


}
