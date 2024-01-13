import flet as ft

def build_page(page: ft.Page):
	page.controls.append(ft.Text("Hello World!"))
	page.update

def main():
	ft.app(
		target=build_page, 
		view=ft.AppView.WEB_BROWSER,
		)

if __name__ == "__main__":
	main()