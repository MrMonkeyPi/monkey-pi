
const CameraPanel = () => {
    return (
        <div class="text-center">
            <img id="stream-img" src={`${location.protocol}//${location.hostname}:8080/?action=stream`} />
        </div>
    )
}

export default CameraPanel;
