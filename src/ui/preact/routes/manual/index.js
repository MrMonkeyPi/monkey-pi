import { useEffect, useState } from "preact/hooks";
import CameraPanel from './camera';
import './style.css';
import WalkPanel from './walk';


const Manual = () => (
	<section id="manual" class="d-flex flex-column justify-content-center main-bg">
		<div class="container">
			<CameraPanel />
			<WalkPanel />

		</div>
	</section>
)


export default Manual;
