
-- Table variable
local data = {["key"]="value"}

-- Domain will be changed on actual Deployment
local url = "http://127.0.0.1:8000/api/dual"

-- Call this function when send button is clicked
function sendDeckList()
    WebRequest.post(url, data, function(request)
        print("sent")
    end)
end
