import { h } from 'preact';
import style from './style.css';
import 'css.gg/icons/css/arrow-up.css'
import 'css.gg/icons/css/arrow-left.css'
import 'css.gg/icons/css/play-stop.css'
import 'css.gg/icons/css/arrow-right.css'
import 'css.gg/icons/css/arrow-down.css'

import 'css.gg/icons/css/chevron-up.css'
import 'css.gg/icons/css/chevron-left.css'
import 'css.gg/icons/css/edit-shadows.css'
import 'css.gg/icons/css/chevron-right.css'
import 'css.gg/icons/css/chevron-down.css'

import 'css.gg/icons/css/airplane.css'

const walk = action => {
	if (!action) return;
	fetch(`/api/robot/walk/${action}`).then(x => x.text()).then(x => console.log(x)).catch(x => console.error(x))
},
	led = (action, arg) => {
		arg = arg || '_'
		fetch(`/api/robot/led/${action}/${arg}`).then(x => x.text()).then(x => console.log(x)).catch(x => console.error(x))
	}


const Home = () => (
	<section id="home" class="d-flex flex-column justify-content-center">
		<div class="container">
			<div>
				<p>I'm <span class="typed" data-typed-items="Developer, Assistant"></span></p>
				<h1>Mr. Monkey Pi</h1>
			</div>

			<div class="position-fixed bottom-0 start-0 end-0 p-3">
				<div class="d-flex justify-content-between">
					<div>
						<p class="text-center">
							<button type="button" class="btn btn-outline-secondary" onClick={() => walk('forward')}>
								<i class="gg-arrow-up"></i>
							</button>
						</p>
						<p class="text-center">
							<button type="button" class="btn btn-outline-secondary" onClick={() => walk('left')}>
								<i class="gg-arrow-left"></i>
							</button>
							<button type="button" class="btn btn-outline-secondary p-2 mx-4" onClick={() => walk('stop')}>
								<i class="gg-play-stop"></i>
							</button>
							<button type="button" class="btn btn-outline-secondary" onClick={() => walk('right')}>
								<i class="gg-arrow-right"></i>
							</button>
						</p>
						<p class="text-center">
							<button type="button" class="btn btn-outline-secondary" onClick={() => walk('back')}>
								<i class="gg-arrow-down"></i>
							</button>
						</p>
					</div>
					<div class="d-flex align-items-end">
						<p class="text-center"><button type="button" class="btn btn-outline-secondary"><i class="gg-airplane"></i></button></p>
					</div>
					<div>
						<p class="text-center"><button type="button" class="btn btn-outline-secondary"><i class="gg-chevron-up"></i></button></p>
						<p class="text-center">
							<button type="button" class="btn btn-outline-secondary"><i class="gg-chevron-left"></i></button>
							<button type="button" class="btn btn-outline-secondary p-2 mx-4" onClick={() => led('loop')}>
								<i class="gg-edit-shadows"></i>
							</button>
							<button type="button" class="btn btn-outline-secondary"><i class="gg-chevron-right"></i></button>
						</p>
						<p class="text-center"><button type="button" class="btn btn-outline-secondary"><i class="gg-chevron-down"></i></button></p>
					</div>
				</div>
			</div>
		</div>
	</section>
);

export default Home;
