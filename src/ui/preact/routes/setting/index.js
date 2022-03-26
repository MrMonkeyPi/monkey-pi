import './style.css';
import { useEffect, useState } from "preact/hooks";


const Setting = () => {
	let checkInfrared = true;
	const [infraredStatus, setinfraredStatus] = useState([true, true]);

	const updateInf = async () => {
		const str = await fetch('/api/robot/sensor/infrared/status').then(x => x.text()),
			result = str.split(',').map(x => x == '1');
		(result.length == 2) && setinfraredStatus(result)
		checkInfrared && updateInf()
	}

	useEffect(() => {
		updateInf()

		return () => {
			checkInfrared = false;
		};
	}, []);

	return (
		<section id="setting" class="d-flex align-items-center main-bg ">
			<div class="container">
				<div>
					<h2>Sensor Calibration </h2>
				</div>

				<div class="panel-box my-5">
					<div class="bg-success bg-opacity-25 border border-success border-1">
						{infraredStatus[0] ? <></> : <div class="sensor-left"></div>}
						{infraredStatus[1] ? <></> : <div class="sensor-right"></div>}
						<div class="spinner-grow text-success opacity-50" role="status">
							<span class="visually-hidden">Scaning...</span>
						</div>
					</div>
					<p>Infrared Sensor</p>
				</div>


				{/* <div class="panel-box">
					<div class="bg-info bg-opacity-25 border border-info border-1">
						<div class="sensor-inner border border-bottom-0"></div>
						<div class="spinner-grow text-info opacity-50" role="status">
							<span class="visually-hidden">Scaning...</span>
						</div>
					</div>
					<p>Ultrasound Sensor</p>
				</div> */}

			</div>
		</section>
	)
};

export default Setting;
