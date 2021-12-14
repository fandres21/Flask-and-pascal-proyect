unit Unit1;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs,
  StdCtrls, ExtCtrls, fphttpclient, fpjson;

const
  inputfield = 'imgs';
  Img1 = '../figuras/a.jpg';
  Img2 = '../figuras/b.jpg';
  Img3 = '../figuras/c.jpg';
  Img4 = '../figuras/d.jpg';
  Img5 = '../figuras/e.jpg';

type
  { TForm1 }
  TForm1 = class(TForm)
    Button1: TButton;
    Button2: TButton;
    Button3: TButton;
    Button4: TButton;
    Button5: TButton;
    Label1: TLabel;
    Memo1: TMemo;
    procedure Button1Click(Sender: TObject);
    procedure Button2Click(Sender: TObject);
    procedure Button3Click(Sender: TObject);
    procedure Button4Click(Sender: TObject);
    procedure Button5Click(Sender: TObject);
    procedure FormCreate(Sender: TObject);
  private

  public

  end;

var
  Form1: TForm1;

implementation

{$R *.lfm}

{ TForm1 }

Procedure TForm1.Button1Click(Sender: TObject);
Var
  Respo: TStringStream;
  S : String;

Begin
  With TFPHttpClient.Create(Nil) do
    try
      Respo := TStringStream.Create('');
      FileFormPost('http://127.0.0.1:4000/data',
                   inputfield,
                   Img1,
                   Respo);
      S := Respo.DataString;
      Memo1.Append('IMG A: ->'+ S);

      Respo.Destroy;
    finally
      Free;
    end;

end;

procedure TForm1.Button2Click(Sender: TObject);
Var
  Respo: TStringStream;
  S : String;

begin
      With TFPHttpClient.Create(Nil) do
    try
      Respo := TStringStream.Create('');
      FileFormPost('http://127.0.0.1:4000/data',
                   inputfield,
                   Img2,
                   Respo);
      S := Respo.DataString;
      Memo1.Append('IMG B: ->'+ S);

      Respo.Destroy;
    finally
      Free;
    end;
end;

procedure TForm1.Button3Click(Sender: TObject);
Var
  Respo: TStringStream;
  S : String;

begin
      With TFPHttpClient.Create(Nil) do
    try
      Respo := TStringStream.Create('');
      FileFormPost('http://127.0.0.1:4000/data',
                   inputfield,
                   Img3,
                   Respo);
      S := Respo.DataString;
      Memo1.Append('IMG C: ->'+ S);

      Respo.Destroy;
    finally
      Free;
    end;
end;

procedure TForm1.Button4Click(Sender: TObject);
Var
  Respo: TStringStream;
  S : String;

begin
      With TFPHttpClient.Create(Nil) do
    try
      Respo := TStringStream.Create('');
      FileFormPost('http://127.0.0.1:4000/data',
                   inputfield,
                   Img4,
                   Respo);
      S := Respo.DataString;
      Memo1.Append('IMG D: ->'+ S);

      Respo.Destroy;
    finally
      Free;
    end;
end;

procedure TForm1.Button5Click(Sender: TObject);
Var
  Respo: TStringStream;
  S : String;

begin
      With TFPHttpClient.Create(Nil) do
    try
      Respo := TStringStream.Create('');
      FileFormPost('http://127.0.0.1:4000/data',
                   inputfield,
                   Img5,
                   Respo);
      S := Respo.DataString;
      Memo1.Append('IMG E: ->'+ S);

      Respo.Destroy;
    finally
      Free;
    end;
end;

procedure TForm1.FormCreate(Sender: TObject);
begin

end;

end.

