class CountOrders extends HTMLElement{
    constructor(){
        super();
        this.shadow = this.attachShadow({ mode: "open" });
		this.styleCSS = `<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css" integrity="sha512-xh6O/CkQoPOWDdYTDqeRdPCVd1SpvCA9XXcUnZS2FmJNp1coAFzvtCN9BmamE+4aHK8yyUHUSCcJHgXloTyT2A==" crossorigin="anonymous" referrerpolicy="no-referrer" />
		<link href="../static/css/bootstrap.min.css" rel="stylesheet">
		<link href="../static/css/bootstrap-extended.css" rel="stylesheet">
		<link href="../static/css/app.css" rel="stylesheet">`
    }

    connectedCallback(){
        this.render();
    }

    render(){
        this.shadow.innerHTML = `
		${this.styleCSS}
		<style>
			
		.card-body:nth-child(2){
			border-radius:100px;
		}
	
		</style>
		<div class="main-card card radius-10">
					<div class="row row-group g-0">
						<div class="col-lg-2 col-md-4 border-radius-left">
							<div class="card-body">
								<div class="d-flex align-items-center">
									<h5 class="mb-0">0</h5>
									<div class="ms-auto">
                                        <i class='fa fa-check fs-5 text-white'></i>
									</div>
								</div>
								<div class="d-flex align-items-center text-white">
									<p class="mt-3 mb-0">Total Orders</p>
								</div>
							</div>
						</div>
						<div class="col-lg-2 col-md-4">
							<div class="card-body">
								<div class="d-flex align-items-center">
									<h5 class="mb-0">0</h5>
									<div class="ms-auto">
                                        <i class='fa fa-pen fs-5 text-white'></i>
									</div>
								</div>
								<div class="d-flex align-items-center text-white">
									<p class="mt-3 mb-0">Active Orders</p>
								</div>
							</div>
						</div>
						<div class="col-lg-2 col-md-4">
							<div class="card-body">
								<div class="d-flex align-items-center">
									<h5 class="mb-0">0</h5>
									<div class="ms-auto">
                                        <i class='fa fa-x fs-5 text-white'></i>
									</div>
								</div>
								<div class="d-flex align-items-center text-white">
									<p class="mt-3 mb-0">Cancelled Orders</p>
								</div>
							</div>
						</div>
						<div class="col-lg-2 col-md-4">
							<div class="card-body">
								<div class="d-flex align-items-center">
									<h5 class="mb-0">0</h5>
									<div class="ms-auto">
                                        <i class='fa fa-repeat fs-5 text-white'></i>
									</div>
								</div>
								<div class="d-flex align-items-center text-white">
									<p class="mt-3 mb-0">Revision Order</p>
								</div>
							</div>
						</div>
						<div class="col-lg-2 col-md-4">
							<div class="card-body">
								<div class="d-flex align-items-center">
									<h5 class="mb-0">0</h5>
									<div class="ms-auto">
                                        <i class='fa fa-stop fs-5 text-white'></i>
									</div>
								</div>
								<div class="d-flex align-items-center text-white">
									<p class="mt-3 mb-0">On Hold Order</p>
								</div>
							</div>
						</div>
						<div class="col-lg-2 col-md-4 border-radius-right">
							<div class="card-body">
								<div class="d-flex align-items-center">
									<h5 class="mb-0">0</h5>
									<div class="ms-auto">
                                        <i class='fa fa-globe fs-5 text-white'></i>
									</div>
								</div>
								<div class="d-flex align-items-center text-white">
									<p class="mt-3 mb-0">Overall</p>
								</div>
							</div>
						</div>
					</div><!--end row-->
				</div>
				`
    }
}


customElements.define('count-orders', CountOrders)