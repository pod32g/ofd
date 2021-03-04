<script lang="ts">
	import axios from "axios";
	import { onMount } from "svelte";

	let last_updated = "";
	let old = {
		size: "",
		timestamp: "",
	};
	let new_obj = {
		size: "",
		timestamp: "",
	};
	let difference = "";

	onMount(async () => {
		const res = await axios.get("http://localhost:8000/api/status");

		const data = res.data;

		last_updated = data.last_updated;
		old = data.old;
		new_obj = data.new;
		difference = data.difference;
	});
</script>

<main>
	<h1>OFD Status</h1>
	<h3>Last Updated: {last_updated}</h3>
	<h3>Size old: {old.size} MB, Updated at: {old.timestamp}</h3>
	<h3>Size new: {new_obj.size} MB, Updated at: {new_obj.timestamp}</h3>
	<h3>Difference: {difference} MB</h3>
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>
