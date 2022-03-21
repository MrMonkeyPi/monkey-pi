import { h } from 'preact';
import { useEffect, useState } from "preact/hooks";
import './style.css';


const Manual = () => {

	return (
		<section id="manual" class="d-flex flex-column justify-content-center">
			<div class="container">
				<div class="text-center">
					<img id="stream" src={`${location.protocol}//${location.hostname}:8080/?action=stream`} />
				</div>

			</div>
		</section>
	)
}

export default Manual;
