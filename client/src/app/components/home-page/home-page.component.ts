import { Component, ElementRef, ViewChild } from '@angular/core';
import { ClientSocketService } from '@app/services/client-socket.service';
import { User } from '@app/classes/user';

@Component({
  selector: 'app-home-page',
  templateUrl: './home-page.component.html',
  styleUrls: ['./home-page.component.scss']
})
export class HomePageComponent {
  @ViewChild("usernameInput") usernameInput!: ElementRef;
  @ViewChild("passwordInput") passwordInput!: ElementRef;
  @ViewChild("dobInput") dobInput!: ElementRef;
  @ViewChild("emailInput") emailInput!: ElementRef;
  username:string = '';
  password:string = '';
  dob:string = '';
  email:string='';

  constructor(private clientSocketService:ClientSocketService) {}

  submit():void {
    const user:User = {username: '', password: '', dob: '', email: ''};
    user.username = this.usernameInput.nativeElement.value;
    user.password = this.passwordInput.nativeElement.value;
    user.dob = this.dobInput.nativeElement.value;
    user.email = this.emailInput.nativeElement.value;
    this.clientSocketService.sendDataToServer(user);
  }

}