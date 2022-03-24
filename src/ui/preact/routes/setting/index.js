import './style.css';

const Setting = () => (
	<section id="setting" class="d-flex align-items-center main-bg ">
		<div class="container">
			<div>
				<h2>Sensor Calibration </h2>
			</div>

			<div class="panel-box my-5">
				<div class="bg-success bg-opacity-25 border border-success border-1">
					<div class="sensor-left"></div>
					<div class="sensor-right"></div>
					<div class="spinner-grow text-success opacity-50" role="status">
						<span class="visually-hidden">Scaning...</span>
					</div>
				</div>
				<p>Infrared Sensor</p>
			</div>


			<div class="panel-box">
				<div class="bg-info bg-opacity-25 border border-info border-1">
					<div class="spinner-grow text-info opacity-50" role="status">
						<span class="visually-hidden">Scaning...</span>
					</div>
				</div>
				<p>Ultrasound Sensor</p>
			</div>

		</div>
	</section>
);

export default Setting;
