import { h } from 'preact';
import { useEffect, useState } from "preact/hooks";
import './style.css';

import 'css.gg/icons/css/arrow-up.css'
import 'css.gg/icons/css/arrow-left.css'
import 'css.gg/icons/css/play-stop.css'
import 'css.gg/icons/css/arrow-right.css'
import 'css.gg/icons/css/arrow-down.css'

import 'css.gg/icons/css/chevron-up.css'
import 'css.gg/icons/css/chevron-left.css'
import 'css.gg/icons/css/chevron-right.css'
import 'css.gg/icons/css/chevron-down.css'
import 'css.gg/icons/css/media-live.css'

import 'css.gg/icons/css/airplane.css'
import 'css.gg/icons/css/volume.css'

const DO = action => {
    if (!action) return;
    fetch(`/api/robot/do/${action}`).then(x => x.text()).then(x => console.log(x))
},
    setCamera = (dir) => {
        fetch(`/api/robot/do/${dir}`)
            .then(() => setTimeout(() => fetch(`/api/robot/do/all_servo_stop`), 200))
    },
    setLED = (r, g, b) => {
        fetch(`/api/robot/led/${r}/${g}/${b}`).then(x => x.text()).then(x => console.log(x))
    },
    getSpeedCss = (speed, self) => speed == self
        ? 'btn btn-primary btn-sm rounded-pill'
        : 'btn btn-outline-primary btn-sm rounded-pill'

const WalkPanel = () => {
    const [speed, setSpeed] = useState(3),
        updateSpeed = s => {
            setSpeed(s)
            fetch(`/api/robot/set/walk_speed/${s}`)
        },
        [autoPilot, setAutoPilot] = useState(false),
        updateAutoPilot = () => {
            setAutoPilot(!autoPilot)
            let action = !autoPilot ? 'auto_pilot' : 'stop_auto_pilot'
            fetch(`/api/robot/do/${action}`)
        },
        [followInfrared, setFollowInfrared] = useState(false),
        updateFollowInfrared = () => {
            setFollowInfrared(!followInfrared)
            let action = !followInfrared ? 'follow_infrared' : 'stop_follow_infrared'
            fetch(`/api/robot/do/${action}`)
        }

    return (
        <div class="action-panel my-5">
            <div class="d-flex justify-content-around thin-panel">
                <div class="speed-panel">
                    <button type="button" class={getSpeedCss(speed, 1)} onClick={() => updateSpeed(1)}>1</button><br />
                    <button type="button" class={getSpeedCss(speed, 2)} onClick={() => updateSpeed(2)}>2</button><br />
                    <button type="button" class={getSpeedCss(speed, 3)} onClick={() => updateSpeed(3)}>3</button><br />
                    <button type="button" class={getSpeedCss(speed, 4)} onClick={() => updateSpeed(4)}>4</button><br />
                    <button type="button" class={getSpeedCss(speed, 5)} onClick={() => updateSpeed(5)}>5</button>
                </div>
                <div class="dir-panel">
                    <p class="text-center">
                        <button type="button" class="btn btn-outline-secondary" onClick={() => DO('forward')}>
                            <i class="gg-arrow-up"></i>
                        </button>
                    </p>
                    <p class="text-center">
                        <button type="button" class="btn btn-outline-secondary" onClick={() => DO('spin_left')}>
                            <i class="gg-arrow-left"></i>
                        </button>
                        <button type="button" class="btn btn-outline-secondary p-2 mx-3" onClick={() => DO('stop')}>
                            <i class="gg-play-stop"></i>
                        </button>
                        <button type="button" class="btn btn-outline-secondary" onClick={() => DO('spin_right')}>
                            <i class="gg-arrow-right"></i>
                        </button>
                    </p>
                    <p class="text-center">
                        <button type="button" class="btn btn-outline-secondary" onClick={() => DO('back')}>
                            <i class="gg-arrow-down"></i>
                        </button>
                    </p>
                </div>
                <div>
                    <p class="text-center">
                        <button type="button" class="btn btn-outline-secondary" onClick={() => setCamera('camera_up')}>
                            <i class="gg-chevron-up"></i>
                        </button>
                    </p>
                    <p class="text-center">
                        <button type="button" class="btn btn-outline-secondary" onClick={() => setCamera('camera_left')}>
                            <i class="gg-chevron-left"></i>
                        </button>
                        <button type="button" class="btn btn-outline-secondary p-2 mx-3" onClick={() => DO('all_servo_stop')}>
                            <a href={`${location.protocol}//${location.hostname}:8080/?action=snapshot`} target="_blank" download={`${Date.now()}.jpg`}>
                                <i class="gg-media-live"></i>
                            </a>
                        </button>
                        <button type="button" class="btn btn-outline-secondary" onClick={() => setCamera('camera_right')}>
                            <i class="gg-chevron-right"></i>
                        </button>
                    </p>
                    <p class="text-center">
                        <button type="button" class="btn btn-outline-secondary" onClick={() => setCamera('camera_down')}>
                            <i class="gg-chevron-down"></i>
                        </button>
                    </p>
                </div>
                <div class="light-panel">
                    <button type="button" class="btn btn-outline-info" onClick={() => setLED(255, 255, 255)}>On</button><br />
                    <button type="button" class="btn btn-outline-danger" onClick={() => setLED(255, 0, 0)}>R</button><br />
                    <button type="button" class="btn btn-outline-success" onClick={() => setLED(0, 255, 0)}>G</button><br />
                    <button type="button" class="btn btn-outline-primary" onClick={() => setLED(0, 0, 255)}>B</button><br />
                    <button type="button" class="btn btn-outline-secondary" onClick={() => setLED(0, 0, 0)}>Off</button>
                </div>
            </div>
            <div class="d-flex justify-content-around my-5 btn-s">
                <button type="button" class="btn btn-outline-secondary" onClick={() => DO('fan')}>Fan</button>
                <button type="button" class={autoPilot ? 'btn btn-outline-danger long-btn' : 'btn btn-outline-primary long-btn'}
                    onClick={() => updateAutoPilot()} >Auto Pilot</button>
                <button type="button" class={followInfrared ? 'btn btn-outline-danger long-btn' : 'btn btn-outline-primary long-btn'}
                    onClick={() => updateFollowInfrared()} >Follow Me</button>
                <button type="button" class="btn btn-outline-secondary" onClick={() => DO('beep')}>Beep</button>
            </div>

        </div>

    )
}

export default WalkPanel;
