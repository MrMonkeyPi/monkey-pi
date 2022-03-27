import { useEffect, useState } from "preact/hooks";

import './style.css';
import 'css.gg/icons/css/play-button-o.css'
import 'css.gg/icons/css/close-o.css'
import 'css.gg/icons/css/check.css'

const runRule = (i) => {
	fetch(`/api/service/rules/execute/${i}`)
},
	saveRules = rules => fetch('/api/service/rules', {
		method: 'POST',
		headers: { 'Content-Type': 'application/json' },
		body: JSON.stringify(rules)
	})

const Service = () => {
	const [rules, setRules] = useState([]),
		[tempRule, setTempRule] = useState(''),
		[isAdding, setIsAdding] = useState(false),
		inputRule = (index, str) => {
			rules[index].rule = str;
			setRules([...rules]);
		},
		deleteRule = (index) => {
			rules[index].isToDelete = true;
			setRules([...rules]);
		},
		saveAllRuls = () => {
			const toSave = rules.filter(x => !x.isToDelete).map(x => ({ rule: x.rule }));
			saveRules(toSave).then(() => {
				setRules(toSave)
				alert('done')
			})
		},
		commitTempRule = () => {
			setIsAdding(false);
			setRules([
				...rules,
				{ isTemp: true, rule: tempRule }
			])
		}

	useEffect(() => {
		fetch('/api/service/rules')
			.then(x => x.json())
			.then(rules => {
				if (Array.isArray(rules) && rules.length) {
					setRules(rules)
					return
				}

				const defaultRules = [
					{ rule: 'sing HappyBirthday' },
					{ rule: 'sing OffWork' },
					{ rule: 'say Hello everyone, I am Mr. Monkey Pi' },
					{ rule: 'say 大家好，我是悟空派' }
				]

				saveRules(defaultRules).then(() => { setRules(defaultRules) })
			})
	}, []);

	return (
		<section id="service" class="d-flex align-items-center main-bg">
			<div class="container">
				<div>
					<h2>Rules</h2>
				</div>
				<div class="my-5">
					{rules.map((r, i) => {
						const tempCss = r.isTemp ? 'btn btn-link disabled' : 'btn btn-link'
						return (
							<p class={r.isToDelete ? 'opacity-25' : ''}>
								<button type="button" class={tempCss} onClick={() => runRule(i)}>
									<i class="gg-play-button-o"></i>
								</button>
								<input class="mx-2 form-control form-control-sm rule-box" type="text" placeholder="Rule String" value={r.rule}
									onChange={(e) => inputRule(i, e.target.value)} />
								<button type="button" class="btn opacity-25 btn_close" onClick={() => deleteRule(i)} ><i class="gg-close-o"></i></button>
							</p>
						)
					})}
					{isAdding ? (<p>
						<button type="button" class="btn btn-link disabled"><i class="gg-play-button-o"></i></button>
						<input class="mx-2 form-control form-control-sm rule-box" type="text" placeholder="Rule String"
							onChange={(e) => setTempRule(e.target.value)} />
						<button type="button" class="btn btn-link" onClick={() => commitTempRule()}><i class="gg-check"></i></button>
					</p>) : null}

					<div class="d-flex justify-content-around my-5 btn-s">
						<button type="button" class="btn btn-outline-primary long-btn" onClick={() => setIsAdding(true)}>Add</button>
						<button type="button" class="btn btn-outline-primary long-btn" onClick={() => saveAllRuls()}>Save</button>
					</div>
				</div>
			</div>
		</section>
	)
};

export default Service;
